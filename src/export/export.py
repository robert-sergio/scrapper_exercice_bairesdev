import pandas as pd
import sqlite3 as sq


class Export:
    def __init__(self, itens) -> None:
        self.itens = itens
        self.df = pd.DataFrame(self.itens)

    def as_sqlite(self, path, tb_name):
        conn = sq.connect(path)
        self.df.to_sql(tb_name, conn, if_exists="replace", index=False)
        conn.close()

    def as_excel(self, path):
        self.df.to_excel(path)

    def as_csv(self, path):
        self.df.to_csv(path)
