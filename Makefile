all: install 

install:
	@poetry install

run:
	@poetry run brain-games

.PHONY: all configure test lint selfcheck check build install