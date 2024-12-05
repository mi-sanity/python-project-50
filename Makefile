setup1: install build publish package-install

setup2: install build publish package-reinstall

setup3: build package-reinstall

gendiff:
	poetry run gendiff

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

ruff-check:
	ruff check --select I

ruff-fix:
	ruff check --fix --select I

isort-fix:
	isort .

.PHONY: install build lint test selfcheck check