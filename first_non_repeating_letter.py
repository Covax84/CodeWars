def first_non_repeating_letter(string: str) -> str:
    """ Input: string (may be empty string)
        Output: first non-repeating character or empty string
    """
    answer = [x for x in string if string.lower().count(x.lower()) == 1]
    return answer[0] if answer else ''
