import argparse
from src.scrapper_by_beautifulsoup import ExtractorBeautifulSoup
from src.scrapper_by_selenium import ExtractorSelenium
from src.scrapper_by_playwright import ExtractorPlayWright

parser = argparse.ArgumentParser()
parser.add_argument(
    "--scrapper_type", dest="scrapper_type", type=str, help="Select the Scrapper Type"
)
parser.add_argument(
    "--validate",
    dest="validate",
    default=False,
    type=str,
    help="Validates the images using Yolo Object Detection",
)
args = parser.parse_args()


class FreeImagesScrapper:

    def __init__(self, args) -> None:
        self.scrapper = args.scrapper_type
        self.validate = bool(args.validate)
        self.num_pages = 1

    def _strategy(self):
        if self.scrapper == "beautifullSoup":
            self.extractor = ExtractorBeautifulSoup
        elif self.scrapper == "selenium":
            self.extractor = ExtractorSelenium
        elif self.scrapper == "playwright":
            self.extractor = ExtractorPlayWright

    def execute(self):
        self._strategy()
        bot = self.extractor(self.validate)
        bot.run(num_pages=self.num_pages, uri="dogs/")
        bot.export()


if __name__ == "__main__":
    run = FreeImagesScrapper(args).execute()
