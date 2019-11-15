def dir_reduc(arr):
    """ Takes an array of strings and returns an array of
        strings with the needless directions removed
        (solution using dictionary)
    """
    dictionary = {"NORTH": "SOUTH", "SOUTH": "NORTH", "WEST": "EAST", "EAST": "WEST"}
    new_arr = []
    for i in arr:
        new_arr.pop() if new_arr and dictionary[i] == new_arr[-1] else new_arr.append(i)
    return new_arr


def dir_reduc_no_dict(arr):
    """ Takes an array of strings and returns an array of
        strings with the needless directions removed
        (solution with no dictionary) - actually can't pass some tests :(
    """
    new_arr = []
    while arr:
        if not new_arr:
            new_arr = [arr[0]]
            arr.remove(arr[0])
        else:
            n = len(new_arr) - 1
            if new_arr[n] == "NORTH" and arr[0] == "SOUTH":
                new_arr.remove(new_arr[n])
                arr.remove(arr[0])
            elif new_arr[n] == "SOUTH" and arr[0] == "NORTH":
                new_arr.remove(new_arr[n])
                arr.remove(arr[0])
            elif new_arr[n] == "WEST" and arr[0] == "EAST":
                new_arr.remove(new_arr[n])
                arr.remove(arr[0])
            elif new_arr[n] == "EAST" and arr[0] == "WEST":
                new_arr.remove(new_arr[n])
                arr.remove(arr[0])
            else:
                new_arr.append(arr[0])
                arr.remove(arr[0])
    return new_arr


def dir_reduc_fork(arr):
    dict = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    res = []
    for i in arr:
        if res and dict[i] == res[-1]:
            res.pop()
        else:
            res.append(i)
    return res
