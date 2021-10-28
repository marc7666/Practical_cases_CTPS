"""
Authorship: Marc Cervera Rosell
"""
from colorama import Fore


def bs_gs(y, g, n):
    """
   We've y = g^x mod n where x = s * i - j =>
   => y = g^(s * i - j) mod n = g^(s * i) * g^(-j) mod n =
   = g^(s * i) * 1/g^j mod n => y * g^j = g^(s * i) mod n
   """
    print(Fore.YELLOW, f"You've entered the following data: y= {y}, g= {g} and n= {n}, so "
                       f"the expression is: {y}^x = {g} (mod {n})")


def print_z(n):
    """
    This method construct the list of Zx
    """
    zx = []
    for i in range(0, n):
        zx.append(int(i))
    return zx


if __name__ == "__main__":
    y = input("Enter the y: ")
    g = input("Enter the g: ")
    n = input("Enter the n: ")
    z = print_z(int(n))
    print(Fore.CYAN, z)
    bs_gs(y, g, n)
