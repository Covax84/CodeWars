def split_to_pairs(s):
    """ splits the string into pairs of two characters.
        If the string contains an odd number of characters then
        it should replace the missing second character of the final pair
        with an underscore ('_'). """
    array = []
    if len(s) % 2 != 0:
        s += '_'
    for i in range(0, len(s)-1, 2):
        array.append(s[i]+s[i+1])
    return array


# print(split_to_pairs("asdfadsf"))    # correct answer: ['as', 'df', 'ad', 'sf']
# print(split_to_pairs("asdfads"))     # correct answer: ['as', 'df', 'ad', 's_']
