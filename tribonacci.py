def tribonacci(signature: list, n: int):
    """ Fibonacci function that given a signature array/list,
        returns the first n elements - signature included of the so seeded sequence. """
    array = [] + signature + [0] * (n - len(signature))
    if n >= 3:
        for i in range(3, n):
            array[i] = array[i - 1] + array[i - 2] + array[i - 3]
        return array
    else:
        return array[:n]
