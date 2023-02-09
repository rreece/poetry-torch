# poetry-torch

[![CI badge](https://github.com/rreece/poetry-torch/actions/workflows/ci.yml/badge.svg)](https://github.com/rreece/poetry-torch/actions)

An example of using poetry to setup a python virtualenv that has pytorch
installed.

This package also shows examples of loading and using HuggingFace
models. So far, all the models used are for NLP.

An analogous project using plain virtualenv instead of poetry is
[venv-torch](https://github.com/rreece/venv-torch).


## How to setup

First time running, install by

```
poetry install
```

Then start the environment by

```
poetry shell
```


## Run sentiment scoring of your input texts

```
cd tests
python test_hf_bert_sentiment.py
```


## Run the tests

```
pytest
```


## How this was created

```
poetry new poetry-torch
cd poetry-torch
cp ~/poetry.toml .
poetry add numpy
poetry add torch --platform linux --python "^3.8"
poetry add transformers
poetry add sentencepiece
poetry add pytest
```


## Author

Ryan Reece ([@rreece](https://github.com/rreece))         
Created: November 2, 2022
