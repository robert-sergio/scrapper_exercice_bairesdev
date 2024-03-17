import pandas as pd
import sqlite3 as sq


class Export:
    def __init__(self, itens) -> None:
        self.itens = itens
        self.df = pd.DataFrame(self.itens)

    def as_sqlite(self):
        conn = sq.connect("db\db_crawlers.sqlite")
        self.df.to_sql("crawlers", conn, if_exists="replace", index=False)
        conn.close()

    def as_excel(self, filename):
        self.df.to_excel(filename)

    def as_csv(self, filename):
        self.df.to_excel(filename)
