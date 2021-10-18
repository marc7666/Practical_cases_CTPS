"""
Authorship: Marc Cervera Rosell
"""

import sys
from colorama import Fore


def is_prime(num):
    """
    This method calculates if a number is prime
    :param num: integer
    :return: True if the number is prime, False otherwise
    """
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    NUMBER = 10011  # First number greater than the given in the instructions
    while not is_prime(NUMBER):
        NUMBER += 1
    print(Fore.YELLOW, "The smallest prime number greater than 10010 is ", NUMBER)
    sys.exit()
