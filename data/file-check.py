import re

if __name__ == "__main__": 
    with open("data/the-verdict.txt", "r") as f:
        raw_text = f.read()

    preprocessed = re.split(r"([,.:;?_!\"']|--|\s)", raw_text)
    preprocessed = [item for item in preprocessed if item.strip()]

    all_words = sorted(set(preprocessed))
    vocab = {token:integer for integer, token in enumerate(all_words)}