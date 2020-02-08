def count_bits(n: int) -> int:
    """ Input: integer n
        Output: number of units in binary representation of n
    """
    return bin(n).count('1')
