class RomanNumerals:
    """ Class-converter:
        Roman numbers to Arabic and vice versa
    """

    convert_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    def __init__(self):
        pass

    def from_roman(self):
        pass

    def to_roman(self):
        pass


cd = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

digit = 9863  # 9863 should give MMMMMMMMM DCCC LX III

if len(str(digit)) > 3:
    my_digit = str(digit)[-3:]
    roman = 'M' * int(str(digit)[:-3]) + ' '
else:
    my_digit = str(digit)
    roman = ''

upper, middle, lower = 100, 50, 10

if len(my_digit) < 2:
    upper, middle, lower = upper // 10, middle // 10, lower // 10
elif len(my_digit) >= 3:
    upper, middle, lower = upper * 10, middle * 10, lower * 10

for i in my_digit:
    if i == '0':
        continue

    if int(i) >= 9:
        roman += cd[lower] * (10 - int(i)) + cd[upper] + ' '
    elif 6 <= int(i) <= 8:
        roman += cd[middle] + cd[lower] * (int(i) - 5) + ' '
    elif 4 <= int(i) <= 5:
        roman += cd[lower] * (5 - int(i)) + cd[middle] + ' '
    elif 1 <= int(i) <= 3:
        roman += cd[lower] * int(i) + ' '

    upper //= 10
    middle //= 10
    lower //= 10

print(roman)
