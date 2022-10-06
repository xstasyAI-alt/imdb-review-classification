import re

HTML_TAG_PATTERN = "<.*?>"


def remove_html_tag(text: str) -> str:
    text_copy = str(text)

    text_copy = re.sub(HTML_TAG_PATTERN, "", text_copy)

    return text_copy


def preprocess_text(text: str) -> str:
    """Preprocess raw text.

    Args:
        text (str): Raw text.

    Returns:
        str: Preprocessed text.
    """
    text_copy = str(text)

    text_copy = remove_html_tag(text_copy)

    return text_copy
