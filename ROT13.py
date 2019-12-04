def rot13(message: str) -> str:
    """ Input: string
        Output: string where every letter replaced with the 13th letter after it, in the alphabet.
    """
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted = ''
    for i in range(len(message)):
        if message[i] in alphabet_upper:
            encrypted += (alphabet_upper[(alphabet_upper.find(message[i]) + 13) % 26])
        elif message[i] in alphabet_lower:
            encrypted += (alphabet_lower[(alphabet_lower.find(message[i]) + 13) % 26])
        else:
            encrypted += message[i]
    return encrypted
