from mock_itens import dummy_itens
from src.export.export import Export
import os


def test_instance():
    instance = Export(dummy_itens)
    assert len(instance.df.columns) == 2


def test_sqlite():
    path = "tests\\export\\teste.sqlite"
    if os.path.exists(path):
        os.remove(path)
    instance = Export(dummy_itens)
    instance.as_sqlite(path)
    assert os.path.exists(path)
    os.remove(path)


def test_csv():
    path = "tests\\export\\teste.csv"
    if os.path.exists(path):
        os.remove(path)
    instance = Export(dummy_itens)
    instance.as_csv(path)
    assert os.path.exists(path)
    os.remove(path)


def test_excel():
    path = "tests\\export\\teste.xlsx"
    if os.path.exists(path):
        os.remove(path)
    instance = Export(dummy_itens)
    instance.as_excel(path)
    assert os.path.exists(path)
    os.remove(path)
