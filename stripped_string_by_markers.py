def string_stripped_by_markers(string: str, markers: list) -> str:
    """ Input: string and list of markers
        Output: stripped string (without everything to the right of the markers)
    """
    array = string.split('\n')
    for i in range(len(array)):
        for marker in markers:
            if marker in array[i]:
                array[i] = array[i][:array[i].index(marker)].strip()
    return '\n'.join(array)


# given params: "apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]
# result should be: "apples, pears\ngrapes\nbananas"
