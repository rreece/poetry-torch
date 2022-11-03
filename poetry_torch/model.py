"""
ModelWrapper using Huggingface pretrained BERT.

See:
https://huggingface.co/docs/transformers/model_doc/bert#transformers.BertForSequenceClassification
"""


import torch
from transformers import BertTokenizer, BertForSequenceClassification


class ModelWrapper:

    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained("textattack/bert-base-uncased-yelp-polarity")
        self.model = BertForSequenceClassification.from_pretrained("textattack/bert-base-uncased-yelp-polarity")

    def run_inference(self, sample):
        inputs = self.tokenizer("Hello, my dog is cute", return_tensors="pt")

        with torch.no_grad():
            logits = self.model(**inputs).logits

        predicted_class_id = logits.argmax().item()
        result = self.model.config.id2label[predicted_class_id]
        return result
