all: install 


install:
	@poetry install

lint: install

run:
	@poetry run brain-games

lint:
	@poetry run flake8 brain_games

.PHONY: all configure test lint selfcheck check build install