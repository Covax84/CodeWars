class Calculator(object):
    """ Alpha version of Calculator class,
    need upgrade to cover all possible cases.
    """

    @staticmethod
    def evaluate(string: str) -> float:  # FIXME!!! consider brackets inside brackets
        my_string = string
        while '(' in my_string:
            inside_brackets = my_string[my_string.index('(') + 1: my_string.index(')')]
            my_string = my_string.replace(f'({inside_brackets})', str(Calculator.calculate(inside_brackets)))
        else:
            return float(Calculator.calculate(my_string))

    @staticmethod
    def calculate(line: str) -> float:  # FIXME!!! order corrupted in case line = '2 + 3 * 4 / 3 - 6 / 3 * 3 + 8'
        arr = line.split()
        i = 0
        while len(arr) != 1:
            if arr[i] == '*':
                arr[i - 1] = float(arr[i - 1]) * float(arr[i + 1])
                arr = arr[:i] + arr[i + 2:]
                i -= 1
            elif arr[i] == '/':
                arr[i - 1] = float(arr[i - 1]) / float(arr[i + 1])
                arr = arr[:i] + arr[i + 2:]
                i -= 1
            elif arr[i] == '+' and ('*' or '/') not in arr[i:]:
                arr[i - 1] = float(arr[i - 1]) + float(arr[i + 1])
                arr = arr[:i] + arr[i + 2:]
                i -= 1
            elif arr[i] == '-' and ('*' or '/') not in arr[i:]:
                arr[i - 1] = float(arr[i - 1]) - float(arr[i + 1])
                arr = arr[:i] + arr[i + 2:]
                i -= 1
            elif arr[i] == '+' or arr[i] == '-' and ('*' or '/') in arr[i:]:
                arr[i + 1] = str(Calculator.calculate(' '.join(arr[i+1:])))
                arr = arr[:i+2]
                i -= 1
            else:
                i += 1
        return arr[0]


print(Calculator.evaluate('2 + 3 * 4 / 3 - 6 / 3 * 3 + 8'))
