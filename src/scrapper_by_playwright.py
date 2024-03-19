from src.playwright_scrapper.freeImages import FreeImages
from src.export.export import Export
from src.logger.logger import logger
from playwright.sync_api import sync_playwright


class ExtractorPlayWright(FreeImages):

    def __init__(self) -> None:
        self.itens = []
        self.status = "initiated"
        self.path_db = "db/db_crawlers.sqlite"
        self.tb_db = "crawlers_playwright"
        logger.info("Started Playwright Crawler")
        super().__init__()

    def __str__(self) -> str:
        return self.status

    def run(self, num_pages):
        with sync_playwright() as playwright:
            chromium = playwright.chromium
            browser = chromium.launch()
            self.page = browser.new_page()

            self.iterate(num_pages)
            self.status = f"finished, {len(self.itens)} itens found in website"

    def iterate(self, num_pages):
        for self.num_page in range(1, num_pages + 1):
            self.dogs()

    def export(self):
        return Export(self.itens).as_sqlite(path=self.path_db, tb_name=self.tb_db)
