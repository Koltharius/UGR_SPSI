import formatter
import hashlib
import random
import sys
from itertools import groupby


def rand_bits_number():
    return str(random.getrandbits(256))


def concatenate(text, number_string):
    return number_string + text


def hash_puzzle(concatenation):
    return hashlib.sha256(concatenation.encode('utf-8 ')).hexdigest()


def hex_to_bin(hexadecimal):
    return bin(int('1' + hexadecimal, 16))[3:]


def print_results(identification, x, h, b, steps):
    print("\nID: ", identification, "\nX: ",
          x, "\nHash: ", h, "\nBinary: ", b, "\nSteps: ", steps)


def puzzle(text, num_bits):
    condition = False
    steps = 0
    number_string = rand_bits_number()
    identification = concatenate(text, number_string)

    while condition != True:
        x = rand_bits_number()
        concatenation = concatenate(text, x)
        h = hash_puzzle(concatenation)
        b = hex_to_bin(h)

        if len(b.split("1", 1)[0]) == num_bits:
            steps += 1
            condition = True
        else:
            steps += 1

    print_results(identification, x, h, b, steps)


if __name__ == '__main__':
    text = open(sys.argv[1], mode='r', encoding='UTF-8')
    num_bits = sys.argv[2]
    puzzle(text.read(), int(num_bits))
