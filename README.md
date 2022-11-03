# poetry-torch

An example of setting up a python virtualenv that has pytorch installed.


## How to setup

```
cd poetry-torch
poetry install
```


## How thist was created

```
poetry new poetry-torch
cp poetry-torch-bak/poetry.toml .
poetry add numpy
poetry add torch --platform linux --python "^3.8"
poetry add transformers
```
