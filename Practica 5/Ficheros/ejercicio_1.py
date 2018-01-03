import hashlib
import random
import sys


def rand_bits_number():
    """return 256 bits random number in String format"""
    return str(random.getrandbits(256))


def concatenate(text, number_string):
    """Concatenate the text and number string and return it"""
    return number_string + text


def hash_puzzle(concatenation):
    """Returns the hexadecimal value of the hash string of the concatenation using sha256"""
    return hashlib.sha256(concatenation.encode('utf-8 ')).hexdigest()


def hex_to_bin(hexadecimal):
    """Convert hexadecimal numbers into binary numbers removing the 0b from the beginning and without deleting the zeros on the left and return it"""
    return bin(int('1' + hexadecimal, 16))[3:]


def print_results(identification, x, h, b, steps):
    """Print the results"""
    print("\nID: ", identification, "\nX: ",
          x, "\nHash: ", h, "\nBinary: ", b, "\nSteps: ", steps)


def puzzle(text, num_bits):
    """Function that generates hash string and converts them into binary until it finds a string that starts with the number of zeros passed as a parameter"""
    condition = False
    steps = 0

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
    if len(sys.argv) != 3:
        print("Bad number of arguemnts. Expected 3 arguments.\nUsage: python3 ejercicio_1.py text_file number_bits")
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
