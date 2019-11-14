all: install 


install:
	@poetry install


run:
	@poetry run brain-games

lint: install
	@poetry run flake8 brain_games

.PHONY: all configure test lint selfcheck check build install