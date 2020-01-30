def spin_words(sentence: str) -> str:
    """
    :param sentence: Text as string
    :return: Same text where words with length >= 5 reversed
    """
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])
