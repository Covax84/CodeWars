def tribonacci(signature: list, n: int) -> list:
    """ Input: 'signature' - an array(first 3 elements of tribonacci sequence) integer: n
        Output: first n elements of tribonacci sequence with 'signature' included.
    """
    array = [] + signature + [0] * (n - len(signature))
    if n >= 3:
        for i in range(3, n):
            array[i] = array[i - 1] + array[i - 2] + array[i - 3]
        return array
    else:
        return array[:n]
