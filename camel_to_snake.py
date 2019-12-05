def to_underscore(string: str) -> str:
    """ Input: CamelCase string or number
        Output: snake_case string
    """
    return ''.join('_' + x.lower() if x.isupper() else x for x in str(string)).lstrip('_')


def to_underscore1(string: str) -> str:
    """ Input: CamelCase string or number
        Output: snake_case string
    """
    return ''.join(map(lambda x: ('_' + x.lower()) if x.isupper() else x, str(string))).lstrip('_')


def to_underscore2(string: str) -> str:
    """ function/method so that it takes CamelCase string and
        returns the string in snake_case notation. Lowercase characters can be numbers.
        If method gets number, it should return string.
    """
    if str(string).isdigit():
        return str(string)
    snake_string = ''
    for i in string:
        if i.isupper():
            snake_string += '_' + i
        else:
            snake_string += i
    return snake_string.lower().lstrip('_')


# print(to_underscore('My3CodeIs4TimesBetter'))  # my3_code_is4_times_better
# print(to_underscore('ThisIsBeautifulDay'))  # this_is_beautiful_day
# print(to_underscore('TestController'))  # test_controller
# print(to_underscore('MoviesAndBooks'))  # movies_and_books
# print(to_underscore('App7Test'))  # app7_test
# print(to_underscore(1))  # "1"
