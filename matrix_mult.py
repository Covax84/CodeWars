def matrix_mult(a: list, b: list) -> list:
    """ Input: two square matrices
        Output: product of matrices
    """
    c = []
    for i in range(len(a)):
        c.append([0] * len(a))
        for j in range(len(a[i])):
            c[i][j] = sum(list(map(lambda x: x[0] * x[1], zip(a[i], list(zip(*b))[j]))))    # not too complicated, eh?
    return c
