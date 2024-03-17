import requests
from bs4 import BeautifulSoup
from datetime import datetime


class IstockPhoto:
    def __init__(self) -> None:
        self.page = 1
        self.header = {
            "Content-Type": "text/html; charset=utf-8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        }
        self.itens = []
        self.message = ""

    def dogs(self):
        url = f"https://www.istockphoto.com/br/search/2/image?mediatype=photography&phrase=dog&page={self.page}"
        response = requests.get(url, headers=self.header)
        if response.status_code != 200:
            self.message = f"Could not get data: status_code {response.status_code}"
            return self.message
        soup = BeautifulSoup(response.content, "html.parser")
        image_gallery = soup.find("div", {"data-testid": "gallery-items-container"})
        image_list = image_gallery.find_all(
            "div", {"data-testid": "gallery-mosaic-asset"}
        )
        for item in image_list:
            data = {
                "page": url,
                "url": item.find("img").attrs["src"],
                "alt": item.find("img").attrs["alt"],
                "date_happened": datetime.now(),
            }
            self.itens.append(data)
        self.message = f"{len(self.itens)} dog pages captured from website"
