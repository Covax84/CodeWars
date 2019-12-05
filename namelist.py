def namelist_old(names: list) -> str:
    """ Given: an array containing hashes of names
        Return: a string formatted as a list of names
        separated by commas except for the last two names,
        which should be separated by an ampersand. """
    answer_string = ''
    for i in range(len(names)):
        if len(names) == 1:
            answer_string += names[i]['name']
            return answer_string
        if i < len(names) - 1:
            answer_string += names[i]['name'] + ', '
        elif i == len(names) - 1:
            answer_string = answer_string[:-2]
            answer_string += ' & ' + names[i]['name']
    return answer_string


def namelist(names: list) -> str:
    """ Input: an array containing hashes of names
        Output: a string formatted as a list of names
        separated by commas except for the last two names,
        which should be separated by an ampersand.
    """
    if len(names) == 1:
        return names[0]['name']
    elif len(names) == 0:
        return ''
    return ', '.join(x['name'] for x in names[:-1]) + ' & {}'.format(names[-1]['name'])


print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggy'}, {'name': 'Homer'}, {'name': 'Marge'}]))
# should return: 'Bart, Lisa, Maggie, Homer & Marge'
