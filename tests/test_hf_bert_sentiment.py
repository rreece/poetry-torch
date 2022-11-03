"""
Test Huggingface pretrained BERT.
"""


from poetry_torch.model import ModelWrapper


model = ModelWrapper()
sample = "Hello, my dog is cute"
result = model.run_inference(sample)

print(result)
