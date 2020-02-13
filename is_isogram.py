def is_isogram(string: str) -> bool:
    """ Input: string
        Output: True if string is an isogram, otherwise False
    """
    my_string = ''
    if string and type(string) is str:
        for letter in string:
            if letter.isalpha():
                my_string += letter.lower()

        for i in range(len(my_string) - 1):
            if my_string.count(my_string[i]) != my_string.count(my_string[i+1]):
                return False
    return True if len(my_string) > 0 else False
