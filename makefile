PROJECT_NAME="SCRAPPERS"

_upgrade:
	@pip install --upgrade pip wheel

_poetry:
	@pip install poetry

_poetry_install:
	@poetry install --no-root

_poetry_shell:
	@poetry shell

_playwright:
	@playwright install

dependencies: _upgrade _poetry _poetry_install _playwright _poetry_shell

test:
	python -m pytest --cov

scrapp-beautifulsoup-yolo:
	python main.py --scrapper_type beautifullSoup --validate True

scrapp-beautifulsoup:
	python main.py --scrapper_type beautifullSoup

scrapp-selenium:
	python main.py --scrapper_type selenium

scrapp-playwright:
	python main.py --scrapper_type playwright

scrapp-all: scrapp-beautifulsoup scrapp-selenium scrapp-playwright