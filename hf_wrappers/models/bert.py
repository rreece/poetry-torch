"""
Handler using Huggingface pretrained BERT.

See:
https://huggingface.co/docs/transformers/model_doc/bert#transformers.BertForSequenceClassification
"""


import os
import torch
from transformers import BertTokenizer, BertForSequenceClassification


class BertHandler:

    def __init__(self, model_name=None):
        if model_name is None:
#            self.model_name = "textattack/bert-base-uncased-yelp-polarity"
            self.model_name = "textattack/bert-base-uncased-SST-2"
        self.tokenizer = BertTokenizer.from_pretrained(self.model_name)
        self.model = BertForSequenceClassification.from_pretrained(self.model_name)

        self.device = None
        if torch.cuda.is_available():
            self.device = torch.device("cuda")
            self.model.to(self.device)

        self.model.eval()

    def run_inference(self, sample):
        inputs = self.tokenizer(sample, return_tensors="pt")

        if self.device is not None:
            inputs = inputs.to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            probs = torch.softmax(logits, dim=1)
            predicted_class_id = probs.argmax().item()
            return predicted_class_id

    def save_checkpoint(self, output_dir):
        output_model_file = os.path.join(output_dir, "pytorch_model.bin")
        output_config_file = os.path.join(output_dir, "config.json")
        output_vocab_file = os.path.join(output_dir, "vocab.txt")
        os.makedirs(output_dir)
        torch.save(self.model.state_dict(), output_model_file)
        self.model.config.to_json_file(output_config_file)
        self.tokenizer.save_vocabulary(output_dir)
