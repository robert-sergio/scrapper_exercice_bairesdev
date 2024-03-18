from threading import Thread
from src.requestsScrapper.freeImages import FreeImages
from src.export.export import Export


class Extractor(FreeImages):
    def __init__(self) -> None:
        self.itens = []
        self.status = "initiated"
        self.path_db = "db\\db_crawlers.sqlite"
        self.tb_db = "crawlers_request"
        super().__init__()

    def __str__(self) -> str:
        return self.status

    def run(self, num_pages):
        self.iterate(num_pages)
        self.status = f"finished, {len(self.itens)} itens found in website"

    def iterate(self, num_pages):
        p = []
        for self.page in range(1, num_pages + 1):
            b = Thread(target=self.dogs, args=[], daemon=False)
            b.start()
            p.append(b)

        for x in p:
            x.join()

    def export(self):
        return Export(self.itens).as_sqlite(path=self.path_db, tb_name=self.tb_db)
