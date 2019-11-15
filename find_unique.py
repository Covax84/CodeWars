def find_uniq(arr: list):
    """ Input: array of numbers, all are equal except one.
        Output: unique number.
    """
    for i in range(len(arr) - 2):
        if arr[i] == arr[i + 1]:
            if arr[i + 1] != arr[i + 2]:
                return arr[i + 2]
        elif arr[i] != arr[i + 1]:
            if arr[i + 1] == arr[i + 2]:
                return arr[i]
            elif arr[i + 1] != arr[i + 2]:
                return arr[i + 1]


def find_uniq2(arr):
    """ Input: array of numbers, all are equal except one.
        Output: unique number.
        v.2.0
    """
    return [n for n in set(arr) if arr.count(n) == 1][0]
