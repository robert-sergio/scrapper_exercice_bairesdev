import argparse
from src.scrapper_by_beautifulsoup import ExtractorBeautifulSoup
from src.scrapper_by_selenium import ExtractorSelenium
from src.scrapper_by_playwright import ExtractorPlayWright

parser = argparse.ArgumentParser()
parser.add_argument(
    "--scrapper_type", dest="scrapper_type", type=str, help="Select the Scrapper Type"
)
args = parser.parse_args()


class Scrapper:

    def __init__(self, scrapper_type) -> None:
        self.scrapper = scrapper_type
        self.num_pages = 15

    def _strategy(self):
        if self.scrapper == "beautifullSoup":
            self.extractor = ExtractorBeautifulSoup
        elif self.scrapper == "selenium":
            self.extractor = ExtractorSelenium
        elif self.scrapper == "playwright":
            self.extractor = ExtractorPlayWright

    def execute(self):
        self._strategy()
        bot = self.extractor()
        bot.run(self.num_pages)
        bot.export()


if __name__ == "__main__":
    run = Scrapper(args.scrapper_type).execute()
