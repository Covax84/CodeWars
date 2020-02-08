def create_phone_number(n: list) -> str:
    """ Input: list of integers
        Output: string of those integers in the form of a phone number: (123) 456-789
    """
    m = ''.join([str(x) for x in n])
    return '({}) {}-{}'.format(m[:3], m[3:-4], m[-4:])
