from datetime import datetime
from src.logger.logger import logger


class FreeImages:

    def __init__(self) -> None:
        self.num_page = 1
        self.itens = []
        self.message = ""
        self.url = "https://www.freeimages.com/search/"
        self.uri = ""
        self.mapped_banners = ["Check our Plans"]
        self.page = None

    def retrieve_images(self):
        skipped = 0
        num_page = self.num_page
        url = f"{self.url}{self.uri}{num_page}"
        self.page.goto(url)
        locators = self.page.get_by_role("article").all()

        if len(locators) == 0:
            self.message = "No data to scrapp"
            return

        for locator in locators:
            item = locator.get_by_role("img").all()[0]
            alt = item.get_attribute("alt")
            src = item.get_attribute("src")

            if alt in self.mapped_banners or "http" not in src:
                skipped = skipped + 1
                continue
            data = {
                "page": url,
                "url": src,
                "alt": alt,
                "date_happened": datetime.now(),
            }
            self.itens.append(data)
        self.message = f"{len(locators)-skipped} images captured from page {num_page}"
        logger.info(f"{len(locators)-skipped} images captured from page {num_page}")
