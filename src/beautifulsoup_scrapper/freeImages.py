import requests
import shutil
import pathlib
from bs4 import BeautifulSoup
from datetime import datetime
from src.logger.logger import logger


class FreeImages:
    def __init__(self) -> None:
        self.num_page = 1
        self.header = {
            "Content-Type": "text/html; charset=utf-8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        }
        self.itens = []
        self.message = ""
        self.mapped_banners = ["Check our Plans"]
        self.url = "https://www.freeimages.com/search/"
        self.uri = ""
        self.name_mapper = {"dogs/": "dog"}

    def retrieve_images(self):
        num_page = self.num_page
        url = f"{self.url}{self.uri}{num_page}"
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
            if "istock-random" in item.attrs.get("class"):
                continue
            src = item.find("img").attrs["src"]
            alt = item.find("img").attrs["alt"]
            if self.validate:
                if not self.validate_yolo(src):
                    continue

            data = {
                "page": url,
                "url": src,
                "alt": alt,
                "date_happened": datetime.now(),
            }
            self.itens.append(data)
        self.message = f"{len(image_list)} images captured from website"
        logger.info(f"{len(image_list)} images captured from page {num_page}")

    def validate_yolo(self, src):
        response = requests.get(src, stream=True)
        temp_path = str(pathlib.Path(__file__).parent.resolve()) + f"/imgs/img_{1}.png"
        with open(temp_path, "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)

        if not self.yolo.check(temp_path, self.name_mapper.get(self.uri)):
            self.message = f"This image is not from a {self.name_mapper.get(self.uri)}"
            return False
        return True
