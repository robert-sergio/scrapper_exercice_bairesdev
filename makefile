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

dependencies: _upgrade _poetry _poetry_install _poetry_shell _playwright

test:
	python -m pytest

scrapp-beautifulsoup:
	python main.py --scrapper_type beautifullSoup

scrapp-selenium:
	python main.py --scrapper_type selenium

scrapp-playwright:
	python main.py --scrapper_type playwright

scrapp-all: scrapp-beautifulsoup scrapp-selenium