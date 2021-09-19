"""
Authorship: Marc Cervera Rosell
"""

import sys
from colorama import Fore


def euclides(dividend, divisor):
    """
    This method calculates the greatest common divisor between two numbers using Euclid's algorithm
    :param dividend: integer
    :param divisor: integer
    :return: integer
    """
    reste = None
    rest_ant = divisor
    if dividend % divisor == 0:
        return divisor

    while reste not in (0, 1):
        reste = dividend % divisor
        aux = divisor
        divisor = reste
        dividend = aux
        if reste != 0:
            rest_ant = reste
    return rest_ant


if __name__ == "__main__":
    print(Fore.YELLOW, "gcd(12, 3) = ", euclides(12, 3))  # gcd = 3
    print(Fore.YELLOW, "gcd(3, 2) = ", euclides(3, 2))  # gcd = 1
    print(Fore.YELLOW, "gcd(15, 8) = ", euclides(15, 8))  # gcd = 1
    print(Fore.YELLOW, "gcd(1032, 180) = ", euclides(1032, 180))  # gcd = 12
    print(Fore.YELLOW, "gcd(275, 225) = ", euclides(275, 225))  # gcd = 25
    sys.exit()
