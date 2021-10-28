import itertools

import exercise_i


# Implementar divisions entre polinomis al estil de division (que retorni quocient i residu)
def poly_addition(poly1, poly2):
    result = [0] * max(len(poly1), len(poly2))
    poly1t = poly1[::-1]
    poly2t = poly2[::-1]
    for i, elem in enumerate(result):
        try:
            result[i] = (poly1t[i] + poly2t[i]) % 5
        except IndexError:
            try:
                result[i] = poly1t[i]
            except IndexError:
                result[i] = poly2t[i]
    while len(result) > 0 and result[0] == 0:
        result = result[1:]
    if result == []:
        return [0]
    return result[::-1]


def poly_multiplication(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i, elem in enumerate(poly1):
        for j, elem2 in enumerate(poly2):
            print(poly1, poly2, i, j, result)
            result[i + j] += (elem * elem2)
    return [elem % 5 for elem in result]


def poly_division_2(poly1, poly2, result):
    if len(poly2) > len(poly1):
        return [0], poly1
    elif len(poly2) == len(poly1):
        q_factor = 0
        while (poly1[0] + poly2[0] * q_factor) % 5 != 0:
            q_factor += 1
            if q_factor == 5:
                raise ValueError
        result[-1] = [q_factor]
        new_poly1 = poly_addition(poly1, poly_multiplication(poly2, result))
        return result, new_poly1
    else:
        q_factor = 0
        while (poly1[0] + poly2[0] * q_factor) % 5 != 0:
            q_factor += 1
            if q_factor == 5:
                raise ValueError
        p_factor = len(poly1) - len(poly2)
        result[len(result) - 1 - p_factor] = [q_factor]
        new_poly1 = poly_addition(poly1, poly_multiplication(poly2, result))
        result = poly_division_2(new_poly1, poly2, result)
        return result, new_poly1


def poly_division(poly1, poly2):
    if len(poly2) > len(poly1):
        return [0], poly1
    elif len(poly2) == len(poly1):
        q_factor = 0
        while (poly1[0] + poly2[0] * q_factor) % 5 != 0:
            q_factor += 1
            if q_factor == 5:
                raise ValueError
        result = [q_factor]
        new_poly1 = poly_addition(poly1, poly_multiplication(poly2, result))
        return result, new_poly1
    else:
        q_factor = 0
        while (poly1[0] + poly2[0] * q_factor) % 5 != 0:
            q_factor += 1
            if q_factor == 5:
                raise ValueError
        p_factor = len(poly1) - len(poly2)
        result = [q_factor] + [0] * p_factor
        new_poly1 = poly_addition(poly1, poly_multiplication(poly2, result))
        result = poly_division_2(new_poly1, poly2, result)
        return result, new_poly1


for comb in itertools.product(range(5), repeat=3):
    div_result = poly_division(comb, [1, 1, 3])
    if div_result[1] == [0]:
        exercise_i.print_polynomial(comb)

