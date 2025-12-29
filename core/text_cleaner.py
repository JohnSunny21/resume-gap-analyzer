import re


def clean_text(text: str) -> str:
    """  
    Cleans raw text for further processing.


    Steps:
    1. Lowercase
    2. Remove Punctuation
    3. Normalize whitespace
    """

    text = text.lower()

    text = re.sub(r"[^a-z0-9\s]"," ",text)

    text = re.sub(r"\s+"," ", text).strip()

    return text



