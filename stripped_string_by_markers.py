def solution(string: str, markers: list) -> str:
    """ Input: string and list of markers
        Output: stripped string (without everything to the right of the markers)
    """
    array = string.split('\n')
    for i in range(len(array)):
        for marker in markers:
            if marker in array[i]:
                array[i] = array[i][:array[i].index(marker)].strip()
    return '\n'.join(array)


# solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
