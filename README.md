# poetry-torch

An example of setting up a python virtualenv that has pytorch installed.


## How to setup

```
cd poetry-torch
poetry install
```


## Run sentiment scoring of your input texts

cd tests
python test_hf_bert_sentiment.py



## How this was created

```
poetry new poetry-torch
cp poetry-torch-bak/poetry.toml .
poetry add numpy
poetry add torch --platform linux --python "^3.8"
poetry add transformers
```
