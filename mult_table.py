def mult_table(n: int) -> print:
    """ Input: integer n
        Output: print multiplication table(first 10 multiplications) for n
    """
    for i in range(1, 11):
        print('{} x {} = {}'.format(n, i, n*i))
