"""
Test Huggingface pretrained BERT.
"""


from poetry_torch.model import ModelWrapper


def test_inference():
    model = ModelWrapper()
    sample = "That dog is cute."
    result = model.run_inference(sample)
    assert result == 1


def main():
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


if __name__ == "__main__":
    main()
