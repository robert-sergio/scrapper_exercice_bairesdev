from datetime import datetime
from src.logger.logger import logger


class FreeImages:

    def __init__(self) -> None:
        self.num_page = 1
        self.itens = []
        self.message = ""
        self.url = "https://www.freeimages.com/"
        self.mapped_banners = ["Check our Plans"]
        self.page = None

    def dogs(self):
        num_page = self.num_page
        url = f"{self.url}{num_page}"
        self.page.goto(url)
        locators = self.page.get_by_role("article").all()

        for locator in locators:
            item = locator.get_by_role("img").all()[0]
            alt = item.get_attribute("alt")
            src = item.get_attribute("src")

            if alt in self.mapped_banners:
                continue
            data = {
                "page": url,
                "url": src,
                "alt": alt,
                "date_happened": datetime.now(),
            }
            self.itens.append(data)
        self.message = f"{len(locators)} dog images captured from page {num_page}"
        logger.info(f"{len(locators)} dog images captured from page {num_page}")
