import requests
from bs4 import BeautifulSoup
from datetime import datetime
from src.logger.logger import logger


class FreeImages:
    def __init__(self) -> None:
        self.page = 1
        self.header = {
            "Content-Type": "text/html; charset=utf-8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        }
        self.itens = []
        self.message = ""
        self.mapped_banners = ["Check our Plans"]

    def dogs(self):
        page = self.page
        url = f"https://www.freeimages.com/search/dogs/{page}"
        response = requests.get(url, headers=self.header)
        if response.status_code != 200:
            self.message = f"Could not get data: status_code {response.status_code}"
            return self.message
        soup = BeautifulSoup(response.content, "html.parser")
        image_gallery = soup.find("div", {"class": "grid-container"})
        image_list = image_gallery.find_all("div", {"class": "grid-item"})
        for item in image_list:
            if item.find("img").attrs["alt"] in self.mapped_banners:
                continue
            data = {
                "page": url,
                "url": item.find("img").attrs["src"],
                "alt": item.find("img").attrs["alt"],
                "date_happened": datetime.now(),
            }
            self.itens.append(data)
        self.message = f"{len(image_list)} dog images captured from website"
        logger.info(f"{len(image_list)} dog images captured from page {page}")
