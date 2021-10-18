"""
Authorship: Marc Cervera Rosell
"""
# pylint: disable=E0401
import sys
from colorama import Fore
import exercise_i

if __name__ == "__main__":
    print(Fore.YELLOW, "gcd(487669403177, 28736540321) = ",
          exercise_i.euclides(487669403177, 28736540321))
    print(Fore.YELLOW, "gcd(20365011074, 12586269023) = ",
          exercise_i.euclides(20365011074, 12586269023))
    print(Fore.YELLOW, "gcd((2**15) - 1, (2**14) - 1) = ",
          exercise_i.euclides(32767, 16383))
    sys.exit()
    # (2**15) - 1 = 32767
    # (2**34) - 1 = 16383
