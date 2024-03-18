PROJECT_NAME="SCRAPPERS"

_upgrade:
	@pip install --upgrade pip wheel

_poetry:
	@pip install poetry

_poetry_install:
	@poetry install --no-root

_poetry_shell:
	@poetry shell

dependencies: _upgrade _poetry _poetry_install _poetry_shell

test:
	python -m pytest --cov

scrapp:
	python main.py