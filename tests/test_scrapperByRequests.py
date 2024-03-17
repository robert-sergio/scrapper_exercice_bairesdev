from src.scrapperByRequests import Extractor


def test_class_instance():
    instance = Extractor()
    assert str(instance) == "initiated"


def test_method_run():
    instance = Extractor()
    instance.run(1)
    assert str(instance) == "finished"
    assert str(instance) == "finished"


def test_method_crawler():
    instance = Extractor()
    instance.run(1)
    assert str(instance) == "finished"
