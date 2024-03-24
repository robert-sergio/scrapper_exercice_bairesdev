from src.scrapper_by_beautifulsoup import ExtractorBeautifulSoup


def test_class_instance():
    instance = ExtractorBeautifulSoup()
    assert str(instance) == "initiated"


def test_method_run():
    instance = ExtractorBeautifulSoup()
    instance.run(1, "dogs/")
    assert str(instance) == "finished, 60 images found in website"


def test_method_crawler():
    instance = ExtractorBeautifulSoup()
    instance.run(1, "dogs/")
    assert str(instance) == "finished, 60 images found in website"
