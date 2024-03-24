import pandas as pd
import sqlite3 as sq
from src.logger.logger import logger


class Export:
    def __init__(self, itens) -> None:
        self.itens = itens
        self.df = pd.DataFrame(self.itens)

    def validate_df(self):
        if len(self.df) > 0:
            return True
        logger.info("No data do save")
        return False

    def as_sqlite(self, path, tb_name):
        if self.validate_df():
            conn = sq.connect(path)
            self.df.to_sql(tb_name, conn, if_exists="replace", index=False)
            conn.close()
            logger.info(f"Saved {len(self.df)} rows to Sqlite, tb {tb_name}")

    def as_excel(self, path):
        if self.validate_df():
            self.df.to_excel(path)
            logger.info(f"Saved {len(self.df)} rows to Excel, tb {path}")

    def as_csv(self, path):
        if self.validate_df():
            self.df.to_csv(path)
            logger.info(f"Saved {len(self.df)} rows to CSV, tb {path}")
