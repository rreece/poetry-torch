# Makefile for poetry-torch

VENV_NAME := .venv

.PHONY: all clean realclean test testclean lock lockclean

all: $(VENV_NAME)
	@echo "\nTo start, please run\npoetry shell\n"

$(VENV_NAME):
	poetry install

clean: testclean
	find python -type f -name '*.py[co]' -exec rm -fv {} +
	find python -type d -name __pycache__  -exec rm -rfv {} +

realclean: clean
	poetry env remove --all

test:
	cd tests && pytest && cd ..

testclean:
	find tests -type f -name '*.py[co]' -exec rm -fv {} +
	find tests -type d -name __pycache__  -exec rm -rfv {} +
	find tests -type d -name .pytest_cache -exec rm -rfv {} +

lock:
	poetry lock

lockclean:
	find . -maxdepth 1 -type f -name poetry.lock -exec rm -fv {} +
