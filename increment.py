def increment_string(strng):
    """ Input: string that ends with a number or not
        Output: if string ends with a number: string with last number incremented by 1,
                otherwise: string with appended number 1.
    """
    num_part = ''
    for i in reversed(strng):
        if i in [str(x) for x in range(10)]:
            num_part += i
        else:
            break
    if num_part:
        n = len(num_part)
        num_part = str(int(num_part[::-1]) + 1)
        return strng[:len(strng)-n:] + num_part.zfill(n)
    return strng + '1'
