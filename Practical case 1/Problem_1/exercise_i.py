"""
Authorship: Marc Cervera Rosell
"""

import sys
from colorama import Fore


def division(dividend, divisor):
    """
    This method implements the division algorithm throughout subtractions.
    :param dividend: integer
    :param divisor: integer
    :return: Will return an integer if divisor != 0 and ArithmeticError otherwise
    """
    if divisor == 0:
        return ArithmeticError
    if divisor > dividend:
        return 0

    quotient = 0
    residue = divisor + 1
    while residue > 0 and residue >= divisor:
        residue = dividend - divisor
        dividend = residue
        quotient += 1
    return quotient, residue


if __name__ == "__main__":
    print(Fore.RED, "In the tuple the first number is the quotient and the"
                    "second one is the reminder")
    print(Fore.YELLOW, "20 // 4 = ", division(20, 4))  # quotient = 5
    print(Fore.YELLOW, "20 // 5 = ", division(20, 5))  # quotient = 4
    print(Fore.YELLOW, "103 // 111 = ", division(103, 111))  # quotient = 0
    print(Fore.YELLOW, "24 // 4 = ", division(24, 4))  # quotient = 6
    print(Fore.YELLOW, "40521 // 16 = ", division(40521, 16))  # quotient = 2532
    sys.exit()
