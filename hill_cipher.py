import numpy as np

key = np.array([[3, 3], [2, 5]])

inverse_key = np.array([[15, 17], [20, 9]])

def encrypt(text):
    text = text.upper().replace(" ", "")

    while len(text) % 2 != 0:
        text += "X"

    result = ""

    for i in range(0, len(text), 2):
        pair = [ord(text[i]) - 65, ord(text[i + 1]) - 65]
        encrypted = np.dot(key, pair) % 26

        result += chr(encrypted[0] + 65)
        result += chr(encrypted[1] + 65)

    return result


def decrypt(text):
    text = text.upper().replace(" ", "")

    result = ""

    for i in range(0, len(text), 2):
        pair = [ord(text[i]) - 65, ord(text[i + 1]) - 65]
        decrypted = np.dot(inverse_key, pair) % 26

        result += chr(decrypted[0] + 65)
        result += chr(decrypted[1] + 65)

    return result.rstrip("X")