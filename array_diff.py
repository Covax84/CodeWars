def array_diff(a: list, b: list) -> list:
    """ Input: 2 arrays (a and b) of integers(optional: any data)
        Output: an array of elements that are present in a and not present in b
    """
    return [x for x in a if x not in b]
