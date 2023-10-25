import string
from random import choice, randrange


def get_code(length):
    code = ''
    count = 1

    while count <= length:
        if randrange(0, 9) % 2 == 0:
            code += choice(string.ascii_letters)
            if randrange(0, 9) % 3 == 0:
                code += choice(string.ascii_uppercase)
            else:
                code += choice(string.ascii_lowercase)
        else:
            code += str(randrange(0, 9))
        count = len(code)

    return code