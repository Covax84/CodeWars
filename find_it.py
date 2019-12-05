def find_it(seq: list) -> int:
    """ Input: an array with only one integer that appears an odd number of times.
        Output: integer that appears an odd number of times.
    """
    freq_dict = dict()
    for integer in seq:             # frequency analysis
        freq_dict[integer] = freq_dict.get(integer, 0) + 1
    for k, v in freq_dict.items():  # return key by value
        if v % 2 != 0:
            return k


def find_it2(seq: list) -> int:
    """ Input: an array with only one integer that appears an odd number of times.
        Output: integer that appears an odd number of times.
        v.2.0
    """
    return [x for x in seq if seq.count(x) % 2 != 0][0]
