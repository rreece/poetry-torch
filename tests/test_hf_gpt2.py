"""
Test Huggingface pretrained BERT.
"""


from poetry_torch.models.gpt2 import GPT2Handler


def test_inference():
    model = ModelWrapper()
    sample = "That dog is cute."
    result = model.run_inference(sample)
    assert result == 1
    sample = "That makes me sick."
    result = model.run_inference(sample)
    assert result == 0


def main():
    model = GPT2Handler()
    
    print("Give a sample of text to prompt GPT2. (q to quit)")
    
    while True:
        print("")
        sample = input("> ").strip()
        if sample.lower() == "q":
            break

        result = model.run_inference(sample)
        generated_text = result[0]["generated_text"]
        print(generated_text)

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
