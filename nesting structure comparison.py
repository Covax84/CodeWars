def same_structure_as(original: list, other: list) -> bool:
    """ Input: two arrays (?) -- one of the tests got int as other
        Output: True if arrays got same nesting structure
        ! Fixed, previous was incorrect, even with the tests passed !
    """
    if type(original) != type(other) or len(original) != len(other):
        return False
    else:
        for i in range(len(original)):
            if isinstance(original[i], (list, set)) and isinstance(other[i], (list, set)):
                if same_structure_as(original[i], other[i]):
                    continue
                else:
                    return False
            elif isinstance(original[i], (int, float, str)) and isinstance(other[i], (int, float, str)):
                continue
            else:
                return False
    return True
