def alphabet_position(text: str) -> str:
    """ Input: text as string
        Output: string with every letter replaced with its position in the alphabet
                replaced characters separated by one space
    """
    return ' '.join([str(ord(x.lower()) - 96) for x in text if x.isalpha()])
