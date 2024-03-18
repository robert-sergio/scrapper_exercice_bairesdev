from src.scrapperByRequests import Extractor
from src.scrapperBySelenium import ExtractorSelenium


def execute_by_requests():
    bot = Extractor()
    bot.run(num_pages=15)
    bot.export()


def execute_by_selenium():
    bot = ExtractorSelenium()
    bot.run(num_pages=15)
    bot.export()


if __name__ == "__main__":
    execute_by_requests()
    execute_by_selenium()
