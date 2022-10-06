import logging
from typing import Union

import pandas as pd

logger = logging.getLogger(__name__)

SEED = 2103


def read_data(filepath: str = "data/imdb-review.csv") -> Union[object, object]:
    """_summary_

    Args:
        filepath (str): _description_

    Returns:
        Union[object, object]: _description_
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        logger.error(f"{filepath} does not exist!")
        return None


def ngram_tokenizer(text, n):
    pass
