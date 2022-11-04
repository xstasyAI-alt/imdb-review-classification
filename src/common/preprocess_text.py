import re

# from nltk import PorterStemmer
# from nltk.corpus import stopwords
from sklearn.base import BaseEstimator, TransformerMixin

# stop = stopwords.words("english")

HTML_TAG_PATTERN = "<.*?>"


class DataTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = self.preprocess_inputs(X)

        return X_

    def preprocess_inputs(self, inputs):
        inputs_ = [self.preprocess_text(input) for input in inputs]

        return inputs_

    def remove_html_tag(self, text: str) -> str:
        text_copy = str(text)
        text_copy = re.sub(HTML_TAG_PATTERN, "", text_copy)
        return text_copy

    def remove_special_case(self, text: str) -> str:
        text_copy = str(text)
        text_copy = re.sub("[^a-zA-Z]+", " ", text_copy)
        return text_copy

    def lower_casing(self, text: str) -> str:
        text_copy = str(text)
        return text_copy.lower()

    # def remove_stop_word(self, text: str) -> str:
    #     text_copy = str(text)
    #     text_copy = " ".join(
    #         [w for w in text_copy.split() if len(w) > 3 and w not in stop]
    #     )
    #     return text_copy

    # def stemming(self, text: str) -> str:
    #     text_copy = str(text)
    #     tokens = text_copy.split()
    #     ps = PorterStemmer()
    #     for i in range(len(tokens)):
    #         tokens[i] = ps.stem(tokens[i])
    #     return " ".join(tokens)

    def preprocess_text(self, text: str) -> str:
        """Preprocess raw text.

        Args:
            text (str): Raw text.

        Returns:
            str: Preprocessed text.
        """
        text_copy = str(text)
        text_copy = self.lower_casing(text_copy)
        text_copy = self.remove_html_tag(text_copy)
        text_copy = self.remove_special_case(text_copy)
        # text_copy = stemming(text_copy)
        # text_copy = remove_stop_word(text_copy)
        text_copy = text_copy.strip()
        return text_copy
