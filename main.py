from src.scrapperByRequests import Extractor
from src.scrapperBySelenium import ExtractorSelenium


def execute_by_requests():
    bot = Extractor()
    bot.run(num_pages=16)
    bot.export()


def execut_by_selenium():
    bot = ExtractorSelenium()
    bot.run(num_pages=16)
    bot.export()
