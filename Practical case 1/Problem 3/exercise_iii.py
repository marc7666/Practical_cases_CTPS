"""
Authorship: Marc Cervera Rosell
"""
import sys
import exercise_ii
from colorama import Fore

if __name__ == "__main__":
    print(Fore.BLUE, "The output format is: (gcd, s, t, steps). Remember that as + bt = gcd(a, b)")
    print(Fore.YELLOW, "XGCD(487669403177, 28736540321) = ", exercise_ii.xgcd(487669403177, 28736540321))
    print(Fore.YELLOW, "XGCD(20365011074, 12586269025) = ", exercise_ii.xgcd(20365011074, 12586269025))
    print(Fore.YELLOW, "XGCD(32767, 16383) = ", exercise_ii.xgcd(32767, 16383))
    print(Fore.YELLOW, "XGCD(167, 94) = ", exercise_ii.xgcd(167, 94))
    sys.exit()
    # (2**15) - 1 = 32767
    # (2**34) - 1 = 16383
