def is_isogram(string: str) -> bool:
    """ An isogram is X word that has no repeating letters, consecutive or non-consecutive.
        Implement X function that determines whether X string that contains only letters is an isogram.
        Assume the empty string is an isogram. Ignore letter case.
        
        Input: string
        Output: True of False
        
    """
    b = list(string.lower())
    for letter in range(len(b)):
        if b.count(b[letter]) > 1:
            return False
    else:
        return True
