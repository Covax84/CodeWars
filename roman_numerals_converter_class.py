class RomanNumerals:
    """ Class-converter:
        Roman numbers to Arabic and vice versa
    """

    @staticmethod
    def from_roman(roman: str) -> int:
        roman_to_arabic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        answer_arabic = 0

        if len(roman) == 1:
            return roman_to_arabic[roman]

        for i in range(len(roman) - 1):
            if roman_to_arabic[roman[i]] >= roman_to_arabic[roman[i + 1]]:
                answer_arabic += roman_to_arabic[roman[i]]
                if i == len(roman) - 2:
                    answer_arabic += roman_to_arabic[roman[i + 1]]
            else:
                answer_arabic += roman_to_arabic[roman[i + 1]] - roman_to_arabic[roman[i]]
        return answer_arabic

    @staticmethod
    def to_roman(arabic: int) -> str:
        arabic_to_roman = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}

        if len(str(arabic)) > 3:
            my_digit = str(arabic)[-3:]
            answer_roman = 'M' * int(str(arabic)[:-3])
        else:
            my_digit = str(arabic)
            answer_roman = ''

        upper, middle, lower = 100, 50, 10

        if len(my_digit) < 2:
            upper, middle, lower = upper // 10, middle // 10, lower // 10
        elif len(my_digit) >= 3:
            upper, middle, lower = upper * 10, middle * 10, lower * 10

        for i in my_digit:
            if i == '0':
                upper //= 10
                middle //= 10
                lower //= 10
                continue

            if int(i) >= 9:
                answer_roman += arabic_to_roman[lower] * (10 - int(i)) + arabic_to_roman[upper]
            elif 6 <= int(i) <= 8:
                answer_roman += arabic_to_roman[middle] + arabic_to_roman[lower] * (int(i) - 5)
            elif 4 <= int(i) <= 5:
                answer_roman += arabic_to_roman[lower] * (5 - int(i)) + arabic_to_roman[middle]
            elif 1 <= int(i) <= 3:
                answer_roman += arabic_to_roman[lower] * int(i)

            upper //= 10
            middle //= 10
            lower //= 10

        return answer_roman
