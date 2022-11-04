import os
from pickle import load

import numpy as np
from dotenv import load_dotenv

from src.common.utils import target_map

load_dotenv()

MODEL_PATH = os.getenv("LOGISTIC_REGRESSION_MODEL_PATH")


class LogisticRegression:
    def __init__(self):
        pass

    def load_model(self):
        self.clf = load(open(MODEL_PATH, "rb"))

    def predict(self, input_text):
        self.load_model()

        pred = self.clf.predict_proba([input_text])[0]

        del self.clf

        return [target_map[np.argmax(pred)], pred]
