"""
Authorship: Marc Cervera Rosell
"""

import sys
from colorama import Fore


def find_divisors(number):
    """
    This method returns a list with the divisors of a number
    :param number: integer
    :return: List of integers
    """
    divisors = []
    i = 0
    while i <= number:
        i += 1
        if number % i == 0:
            divisors.append(i)
    return divisors


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


# pylint: disable=C0200
def prime_divisors(number):
    """
    This method calculates the prime divisors of a number
    :param number: integer
    :return: A list of integers that contains the all the prime divisors of the number
    """
    divisors = find_divisors(number)
    primes = []
    for i in range(0, len(divisors)):
        if is_prime(divisors[i]):
            primes.append(divisors[i])
    return primes


def prime_factors(num):
    """
    This method calculates the prime factors of a number
    :param num: integer
    :return: A list of integers that contains the prime factors of the given number
    """
    prime_divs = prime_divisors(num)
    prime_facts = []
    quotient = None
    while quotient != 1:
        for i in range(len(prime_divs) - 1, 0, -1):
            if quotient != 1:
                quotient = num / prime_divs[i]
                num = quotient
                prime_facts.append(prime_divs[i])
    return prime_facts


if __name__ == "__main__":
    print(Fore.YELLOW, "Prime factors of 30: ", prime_factors(30))  # [5,3,2]
    print(Fore.YELLOW, "Prime factors of 36: ", prime_factors(36))  # [3,2,3,2]
    print(Fore.YELLOW, "Prime factors of 1245: ", prime_factors(1245))  # [85,5,3]
    print(Fore.YELLOW, "Prime factors of 500: ", prime_factors(500))  # [5,5,5,2,2]
    sys.exit()
