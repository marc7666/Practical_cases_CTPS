"""
Authorship: Marc Cervera Rosell
"""
from colorama import Fore
import exercise_i

if __name__ == "__main__":
    print(Fore.RED, "NOTE: To know the result, look for the green sentence."
                    " You'll see it before the yellow sentence that indicates the case")
    print(Fore.YELLOW, "-------------------- Case 3^x = 12 mod 29 --------------------")
    exercise_i.bs_gs(12, 3, 29)
    print(Fore.YELLOW, "-------------------- Case 13^x = 19 mod 71 --------------------")
    exercise_i.bs_gs(19, 13, 71)
    print(Fore.YELLOW, "-------------------- Case 7^x = 50 mod 143 --------------------")
    exercise_i.bs_gs(50, 7, 143)
