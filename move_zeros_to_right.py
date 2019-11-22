def move_zeros(array):
    """ Input: array
        Output: same array with all the zeros moved to the end.
    """
    new_array = []
    for elem in array:
        if type(elem) == float and elem == 0.0:
            continue
        elif type(elem) == int and elem == 0:
            continue
        new_array.append(elem)
    array = new_array + [0] * (len(array) - (len(new_array)))
    return array


print(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))

print(move_zeros([0, 0, 0, 0, 0, 0, 0, 'a', 'b', None, 'c', 'd', 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0]))
# [0, 0, 0, 0, 0, 0, 0, 1, 1, 3, 1, 9, 9, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 1, 1, 3, 1, 9, 9, 0, 0, 0]
# ['a', 'b', None, 'c', 'd', 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ['a', 'b', None, 'c', 'd', False, [], {}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
# [ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ]

# print(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
# [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#
# print(move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
# # ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# print(move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]))
# # ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
#
# print(move_zeros([0, 1, None, 2, False, 1, 0]))  # [1,None,2,False,1,0,0])
# print(move_zeros(["a", "b"]))  # ["a","b"])
# print(move_zeros(["a"]))  # ["a"])
# print(move_zeros([0, 0]))  # [0,0]

# def move_zeros(array):
#     new_array = []
#     for elem in array:
#         if type(elem) == float and elem == 0.0:
#             continue
#         elif type(elem) == int and elem == 0:
#             continue
#         new_array.append(elem)
#     array = new_array + [0] * (len(array) - (len(new_array)))
#     return array
#
