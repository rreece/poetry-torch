
VENV_NAME := ".venv"

all: $(VENV_NAME)
	@echo "\nTo start, please run\npoetry shell"

$(VENV_NAME):
	poetry install

clean: testclean
	find . -type f -name '*.py[co]' -exec rm -fv {} +
	find . -type d -name __pycache__  -exec rm -rfv {} +

realclean: clean
	poetry env remove --all

test:
	pytest

testclean:
	find . -type d -name .pytest_cache -exec rm -rfv {} +

lock:
	poetry lock

lockclean:
	find . -maxdepth 1 -type f -name poetry.lock -exec rm -fv {} +
