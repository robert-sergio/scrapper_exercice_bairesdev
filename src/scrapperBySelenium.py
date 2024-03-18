from threading import Thread
from seleniumScrapper.istockphoto import IstockPhoto
from export.export import Export


class ExtractorSelenium(IstockPhoto):

    def __init__(self) -> None:
        self.itens = []
        self.status = "initiated"
        self.path_db = "db\\db_crawlers.sqlite"
        self.tb_db = "crawlers_selenium"
        super().__init__()

    def __str__(self) -> str:
        return self.status

    def run(self, num_pages):
        self.handle_login()
        self.iterate(num_pages)
        self.handle_logout()
        self.status = f"finished"

    def iterate(self, num_pages):
        for self.page in range(1, num_pages + 1):
            self.dogs()

    def export(self):
        return Export(self.itens).as_sqlite(path=self.path_db, tb_name=self.tb_db)


if __name__ == "__main__":
    bot = ExtractorSelenium()
    bot.run(10)
    bot.export()
