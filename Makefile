all: install 

install:
	@poetry install

run:
	@poetry run brain-games

lint:
	@sudo cd /home/nick/python-project-lvl1
	@poetry run flake8 brain_games

.PHONY: all configure test lint selfcheck check build install