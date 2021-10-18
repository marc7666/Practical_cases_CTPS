"""
Authorship: Marc Cervera Rosell
"""


# pylint: disable=C0103
def xgcd(a, b):
    """
    This method calculates the XGCD and returns as the outpu a tuple of 4 positions with the gcd,
    the two coefficients of the Bezout's identity and the number of steps
    """
    steps = 0
    if b == 0:
        gcd, s, t = a, 1, 0
        return gcd, s, t, steps

    s2, t2, s1, t1 = 1, 0, 0, 1
    while b > 0:
        q = a // b
        residue, s, t = (a - b * q), (s2 - q * s1), (t2 - q * t1)
        a, b, s2, t2, s1, t1 = b, residue, s1, t1, s, t
        steps += 1
    gcd, s, t = a, s2, t2
    return gcd, s, t, steps
