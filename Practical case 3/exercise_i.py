"""
Authorship: Marc Cervera Rosell
"""
import math
from colorama import Fore


# pylint: disable=C0103
# pylint: disable=W0621
def build_list_1(y, g, n, s):
    """
    This method builds the first list and returns it
    """
    list1 = []
    for j in range(0, s + 1):
        list1.append(((y * (g ** j)) % n, j))
    return list1


# pylint: disable=C0103
# pylint: disable=W0621
def build_list_2(g, n, s):
    """
    This method builds the second list and returns it
    """
    list2 = []
    for i in range(0, s + 1):
        list2.append((g ** (s * i) % n, s * i))
    return list2


# pylint: disable=C0103
# pylint: disable=W0621
# pylint: disable=W0612
def search_match(list1, list2):
    """
    This method searches for a match between the two lists
    """
    for i in range(0, len(list1)):
        for j in range(len(list1)):
            if list1[i][0] == list2[j][0]:
                return list1[i], list2[j]
    '''for i in range(0, len(list1) - 1):
        for j in range(0, len(list1) - 1):
            for k in 0, 1:
                if list1[i][0] == list2[j][0]:
                    return list1[i], list2[j]'''


# pylint: disable=C0103
# pylint: disable=W0621
def bs_gs(y, g, n):
    """
   We've y = g^x mod n where x = s * i - j =>
   => y = g^(s * i - j) mod n = g^(s * i) * g^(-j) mod n =
   = g^(s * i) * 1/g^j mod n => y * g^j = g^(s * i) mod n
   """
    print(Fore.MAGENTA, f"You've entered the following data: y= {y}, g= {g} and n= {n}, so "
                        f"the expression is: {y} = {g}^x (mod {n})")
    s = math.ceil(math.sqrt(int(n)))  # ceil => function that rounds up a number upwards
    print(Fore.CYAN, f"The value of s is {s}. So, the values of 'i' and "
                     f"'j' will run in 0, ..., {s}")
    print(Fore.MAGENTA, f"Now we've to create two lists. The first (L1) will contain the tuple "
                        f"([y * g^j] mod n, j)"
                        f" and the second one (L2) will contain the tuple "
                        f"([g^(s * i)] mod n, [s * i]).\n "
                        f"So the first list is going to look like: ([{y} * {g}^(j)] mod {n}, j)"
                        f" and the second one:"
                        f"([{g}^({s} * i) mod {n}], [{s} * i])")
    list1 = build_list_1(y, g, n, s)
    list2 = build_list_2(g, n, s)
    print(Fore.CYAN, "List 1 = ", list1)
    print(Fore.CYAN, "List 2 = ", list2)
    print(Fore.MAGENTA, "Once we've the two lists, we've to search for a match with"
                        " the first component of the tuple")
    match1, match2 = search_match(list1, list2)
    print(Fore.CYAN, f"The match is between the tuples {match1} of the first list and"
                     f" {match2} of the second list")
    x_value = match2[1] - match1[1]
    print(Fore.GREEN, f"The x value is: {x_value}")


if __name__ == "__main__":
    y = input("Enter the y: ")
    g = input("Enter the g: ")
    n = input("Enter the n: ")
    bs_gs(int(y), int(g), int(n))
