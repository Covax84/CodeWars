def to_underscore(string):
    """ Input: CamelCase string or number
        Output: snake_case string
    """
    return ''.join('_' + x.lower() if x.isupper() else x for x in str(string)).lstrip('_')


def to_underscore1(string: str):
    """ Input: CamelCase string or number
        Output: snake_case string
    """
    return ''.join(map(lambda x: ('_' + x.lower()) if x.isupper() else x, str(string))).lstrip('_')


def to_underscore2(string):
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


int(to_underscore('My3CodeIs4TimesBetter'))
print(to_underscore('ThisIsBeautifulDay'))
print(to_underscore('TestController'))  # returns test_controller
print(to_underscore('MoviesAndBooks'))  # returns movies_and_books
print(to_underscore('App7Test'))  # returns app7_test
print(to_underscore(1))  # returns "1"
