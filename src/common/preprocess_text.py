import re

import numpy as np
import pandas as pd
from nltk import PorterStemmer
from nltk.corpus import stopwords

stop = stopwords.words("english")

HTML_TAG_PATTERN = "<.*?>"


def remove_html_tag(text: str) -> str:
    text_copy = str(text)
    text_copy = (
        re.sub(HTML_TAG_PATTERN, "", text_copy)
    )
    return text_copy


def remove_special_case(text: str) -> str:
    text_copy = str(text)
    text_copy = re.sub("[^a-zA-Z]+", " ", text_copy)
    return text_copy


def lower_casing(text: str) -> str:
    text_copy = str(text)
    return text_copy.lower()


def remove_stop_word(text: str) -> str:
    text_copy = str(text)
    text_copy = " ".join([w for w in text_copy.split() if len(w) > 3 and w not in stop])
    return text_copy


def stemming(text: str) -> str:
    text_copy = str(text)
    tokens = text_copy.split()
    ps = PorterStemmer()
    for i in range(len(tokens)):
        tokens[i] = ps.stem(tokens[i])
    return " ".join(tokens)


def preprocess_text(text: str) -> str:
    """Preprocess raw text.

    Args:
        text (str): Raw text.

    Returns:
        str: Preprocessed text.
    """
    text_copy = str(text)
    text_copy = remove_html_tag(text_copy)
    text_copy = remove_special_case(text_copy)
    text_copy = lower_casing(text_copy)
    text_copy = stemming(text_copy)
    text_copy = remove_stop_word(text_copy)
    return text_copy


def main():
    path = (
        link
    ) = "C:/Users/Chi Khang/Documents/imdb-review-classification/data/train.csv"
    data = pd.read_csv(path)
    data["clean_review"] = np.vectorize(preprocess_text)(data["review"])
    print(data["review"][0])
    print(data["clean_review"][0])


if __name__ == "__main__":
    main()
