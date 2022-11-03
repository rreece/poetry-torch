"""
Test Huggingface pretrained BERT.
"""


from poetry_torch.model import ModelWrapper


model = ModelWrapper()

print("Give a sample of text to score its sentiment.")

done = False
while not done:
    print("")
    sample = input("> ").strip()
    result = model.run_inference(sample)
    print(result)

    print("")
    choice = input("Are you done? [y/n] > ").strip().lower()
    done = choice == "y"

print("Done.")
