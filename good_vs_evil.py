def goodVsEvil(good: str, evil: str) -> str:
    """ Input: two strings with the number of good and evil units.
        Output: battle result message.
        
        For actual understanding read kata description:
        https://www.codewars.com/kata/good-vs-evil/train/python
    """
    good_units = {0: 1, 1: 2, 2: 3, 3: 3, 4: 4, 5: 10}
    evil_units = {0: 1, 1: 2, 2: 2, 3: 2, 4: 3, 5: 5, 6: 10}

    good_arr = good.split()
    evil_arr = evil.split()

    good_power = 0
    evil_power = 0

    for i in range(len(good_arr)):
        good_power += int(good_arr[i]) * good_units[i]
    for i in range(len(evil_arr)):
        evil_power += int(evil_arr[i]) * evil_units[i]

    if good_power - evil_power > 0:
        return "Battle Result: Good triumphs over Evil"
    elif good_power - evil_power < 0:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"
    
