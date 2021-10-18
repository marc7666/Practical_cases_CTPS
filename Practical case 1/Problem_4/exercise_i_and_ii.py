"""
Authorship: Marc Cervera Rosell
"""
import sys
from colorama import Fore
import XGCD

if __name__ == "__main__":
    result1 = XGCD.xgcd(487669403177,28736540321)
    print(Fore.YELLOW, "The inverse of 28736540321 (mod 487669403177) =", result1[2] % 487669403177)
    result2 = XGCD.xgcd(20365011074, 12586269025)
    print(Fore.YELLOW, "The inverse of 12586269025 (mod 20365011074) =", result1[2] % 20365011074)
    sys.exit(0)