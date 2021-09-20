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
    print(Fore.YELLOW, "gcd((2**35) - 1, (2**34) - 1) = ",
          exercise_i.euclides(34359738367, 17179869183))
    sys.exit()
    # (2**35) - 1 = 34359738367
    # (2**34) - 1 = 17179869183
