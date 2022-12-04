
all: .venv

.venv:
	poetry install

clean:
	poetry env remove --all
	find . -type f -name '*.py[co]' -exec rm -fv {} +
	find . -type d -name __pycache__  -exec rm -rfv {} +
	find . -type d -name .pytest_cache -exec rm -rfv {} +

realclean: clean
	find . -maxdepth 1 -type f -name poetry.lock -exec rm -fv {} +
