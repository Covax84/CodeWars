def unique_in_order(iterable: any) -> list:
    """
    :param: any iterable
    :return: list of items without any elements with the same value next to each other
             and preserving the original order of elements
    """
    output_arr = [iterable[0]] if iterable else []
    for i in iterable:
        if i != output_arr[-1]:
            output_arr.append(i)
        continue
    return output_arr
