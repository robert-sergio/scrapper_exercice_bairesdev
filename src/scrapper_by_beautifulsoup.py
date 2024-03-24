from threading import Thread
from src.beautifulsoup_scrapper.freeImages import FreeImages
from src.export.export import Export
from src.logger.logger import logger
from src.check_images.yolo_verification import Detection


class ExtractorBeautifulSoup(FreeImages):
    def __init__(self, validate=False) -> None:
        self.validate = validate
        self.itens = []
        self.status = "initiated"
        self.path_db = "db/db_crawlers.sqlite"
        self.tb_db = "crawlers_beautifulsoup"
        if self.validate:
            self.yolo = Detection()
        super().__init__()
        logger.info("Started Requests & BeautifulSoup Crawler")

    def __str__(self) -> str:
        return self.status

    def run(self, num_pages, uri):
        self.uri = uri
        self.iterate(num_pages)
        self.status = f"finished, {len(self.itens)} images found in website"

    def iterate(self, num_pages):
        p = []
        for self.num_page in range(1, num_pages + 1):
            b = Thread(target=self.retrieve_images, args=[], daemon=False)
            b.start()
            p.append(b)

        for x in p:
            x.join()

    def export(self):
        return Export(self.itens).as_sqlite(path=self.path_db, tb_name=self.tb_db)
