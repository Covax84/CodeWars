def find_outlier(integers: list):
    """ Input: array of integers.
        Output: array element that is a single odd or a single even number.
        No memory waste ;)
    """
    for i in range(len(integers) - 2):
        if integers[i] % 2 == integers[i + 1] % 2:
            if integers[i + 1] % 2 != integers[i + 2] % 2:
                return integers[i + 2]
        elif integers[i] % 2 != integers[i + 1] % 2:
            if integers[i + 1] % 2 == integers[i + 2] % 2:
                return integers[i]
            elif integers[i + 1] % 2 != integers[i + 2] % 2:
                return integers[i + 1]


print(find_outlier([2, 4, 3]))  # 3
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))  # 11
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))  # 160
