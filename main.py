import argparse
from src.scrapperByBeautifulSoup import Extractor
from src.scrapperBySelenium import ExtractorSelenium

parser = argparse.ArgumentParser()
parser.add_argument(
    "--scrapper_type", dest="scrapper_type", type=str, help="Select the Scrapper Type"
)
args = parser.parse_args()


class Scrapper:

    def __init__(self, scrapper_type) -> None:
        self.scrapper = scrapper_type

    def _strategy(self):
        if self.scrapper == "beautifullSoup":
            self.extractor = Extractor
        elif self.scrapper == "selenium":
            self.extractor = ExtractorSelenium

    def execute(self):
        self._strategy()
        bot = self.extractor()
        bot.run(num_pages=15)
        bot.export()


if __name__ == "__main__":
    run = Scrapper(args.scrapper_type).execute()
