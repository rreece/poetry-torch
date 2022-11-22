# poetry-torch

An example of using poetry to setup a python virtualenv that has pytorch
installed.


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


## How this was created

```
poetry new poetry-torch
cp poetry-torch-bak/poetry.toml .
poetry add numpy
poetry add torch --platform linux --python "^3.8"
poetry add transformers
poetry add pytest
```


## Run the tests

Just call

```
pytest
```

There are some warnings we should work on, but everything should pass.
