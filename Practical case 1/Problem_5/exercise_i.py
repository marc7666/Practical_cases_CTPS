"""
Authorship: Marc Cervera Rosell
"""

import itertools

from colorama import Fore


# pylint: disable=C0200
def convert_to_z5(numbers):
    """
    This method converts all the factors of the polynomial to Z5
    """
    result = []
    for i in range(0, len(numbers)):
        aux = numbers[i] % 5
        result.append(aux)
    return result


# The factors will be like: [x,y,z]
def print_polynomial(factors):
    """
    This method convert the list of factors to correspondent polynomial
    """
    if len(factors) == 0:
        return "0"

    polynomial_str = ""
    converted = convert_to_z5(factors)
    for i in range(0, len(factors) - 1):
        if converted[i] == 0:
            continue

        polynomial_str += str(converted[i])
        polynomial_str += "*x**"
        power = len(converted) - 1 - i
        polynomial_str += str(power)
        polynomial_str += "+"
    polynomial_str += str(converted[len(converted) - 1])
    return polynomial_str


if __name__ == "__main__":
    for p in itertools.product(range(5), repeat=3):
        print(Fore.YELLOW, print_polynomial(p))
