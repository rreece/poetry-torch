
all:
	poetry install

clean:
	rm -f poetry.lock
	poetry env remove --all
