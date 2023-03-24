from itertools import permutations
from math import sqrt, ceil


def is_prime(num) -> bool:
    num = abs(num)
    loop = 2
    if num < loop:
        return False
    while loop**2 < num + 1:
        if num % loop == 0:
            return False
        loop += 1
    return True


def prime_sieve(limit):
    prime = [True for _ in range(limit + 1)]
    finalised = []
    p = 2
    while p**2 <= limit:
        print
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    for i in range(2, len(prime)):
        if prime[i]:
            finalised.append(i)

    return finalised  # returns list


def prime_sieve_and_pandigital(limit):
    prime = [True for _ in range(limit + 1)]
    finalised = []
    p = 2
    while p**2 <= limit:
        print
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    for i in range(2, len(prime)):
        if prime[i] and is_pandigital(str(i)):
            print(i)
            finalised.append(i)

    return finalised  # returns list


def get_factors_dict(num):
    n = 1
    factors = dict()
    while n**2 <= num:
        if num % n == 0 and not (n in factors or num // n in factors):
            factors[n] = num // n
        n += 1
    return factors


def get_factors(num) -> set:
    n = 1
    factors = set()
    while n**2 <= num:
        if num % n == 0:
            factors.add(n)
            factors.add(num // n)
        n += 1
    return factors


def get_all_permutations(string: str) -> list:
    # itertools coming in clutch
    all_permutations = [
        "".join(i) for i in list(permutations(string, len(string)))
    ]
    return all_permutations


def get_all_rotations(string: str) -> list:
    """for 123, returns 123, 312, 231"""
    rotations = set()
    original_string = string
    rotations.add(string)
    string = string[-1] + string[:-1]
    while string != original_string:
        rotations.add(string)
        string = string[-1] + string[:-1]
    return list(rotations)


def is_pandigital(string: str, comparison_string="123456789") -> bool:
    length = len(str(string))
    comparison_string = ""
    for i in range(1, length + 1):
        comparison_string += str(i)
    if set(string) == set(comparison_string) and len(string) == len(
            comparison_string):
        return True
    return False


def generate_pythagorean_triples(limit: int):
    """https://www.youtube.com/watch?v=QJYmyhnaaek"""
    triples = []
    upper_bound_for_side = ceil(sqrt(limit))
    for a in range(1, upper_bound_for_side):
        for b in range(1, upper_bound_for_side):
            if a**2 + b**2 <= limit:
                abc = [abs(a**2 - b**2), 2 * a * b, a**2 + b**2]
                scalar = 1
                new_abc = [1, 1, 1]
                while new_abc[2] <= limit:
                    new_abc = [i * scalar for i in abc]
                    if new_abc not in triples and 0 not in new_abc:
                        triples.append(new_abc)
                    scalar += 1
    return triples


def get_place_in_alphabet(char: str):
    char = char.lower()
    return ord(char) - 96


def generate_triangle_numbers(limit: int) -> list:
    i = 1
    tri_num = []
    increment_by = 2
    while i <= limit:
        tri_num.append(i)
        i += increment_by
        increment_by += 1
    return tri_num


def is_pentagonal(num):
    return True if (1 / 6) * (sqrt(24 * num + 1) + 1) % 1 == 0 else False


def generate_pentagonal_numbers(limit):
    most_recent_num = 0
    i = 1
    nums = set()
    while most_recent_num < limit:
        most_recent_num = (i * (3 * i - 1)) // 2
        nums.add(most_recent_num)
        i += 1
    return sorted(nums)


def is_triangular(num):
    if (1 / 2) * (sqrt(8 * num + 1) - 1) % 1 == 0:
        return True
    else:
        return False


def is_hexagonal(num):
    if ((1 / 4) * (1 + sqrt(8 * num + 1))) % 1 == 0:
        return True
    else:
        return False


def get_distinct_prime_factors(num):
    factors = [i for i in get_factors(num) if is_prime(i)]
    return factors
