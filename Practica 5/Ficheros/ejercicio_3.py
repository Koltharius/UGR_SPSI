import hashlib
import random
import sys


def rand_bits_number():
    return str(random.getrandbits(256))


def concatenate(text, number_string):
    return number_string + text


def hash_puzzle(concatenation):
    return hashlib.sha256(concatenation.encode('utf-8 ')).hexdigest()


def hex_to_bin(hexadecimal):
    return bin(int('1' + hexadecimal, 16))[3:]


def add_one(x):
    return str(int(x) + int(1))


def print_results(identification, x, h, b, steps):
    print("\nID: ", identification, "\nX: ",
          x, "\nHash: ", h, "\nBinary: ", b, "\nSteps: ", steps)


def puzzle(identification, num_bits):
    condition = False
    steps = 0
    x = rand_bits_number()
    concatenation = concatenate(text, x)
    h = hash_puzzle(concatenation)
    b = hex_to_bin(h)

    while condition is not True:
        if len(b.split("1", 1)[0]) == num_bits:
            steps += 1
            condition = True
        else:
            x = add_one(x)
            concatenation = concatenate(text, x)
            h = hash_puzzle(concatenation)
            b = hex_to_bin(h)
            steps += 1

    print_results(identification, x, h, b, steps)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error: Bad number of arguemnts. Expected 3 arguments")
        print("Usage: python3 ejercicio_1.py text_file number_bits")
        sys.exit(1)

    try:
        fh = open(sys.argv[1], mode='r', encoding='UTF-8')
        text = fh.read()
        fh.close()
        num_bits = int(sys.argv[2])
        if num_bits <= 0:
            raise incorrect_num_bits

    except IOError:
        print("Error: Could not read file", sys.argv[1])
        sys.exit(2)

    except Exception as incorrect_num_bits:
        print("Error: The input", num_bits, "number is less than 0")
        sys.exit(3)

    number_string = rand_bits_number()
    identification = concatenate(text, number_string)
    puzzle(identification, num_bits)
