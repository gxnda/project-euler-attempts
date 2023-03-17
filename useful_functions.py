from itertools import permutations


def is_prime(num) -> bool:
    num = abs(num)
    loop = 2
    if num < loop:
        return False
    while loop ** 2 < num + 1:
        if num % loop == 0:
            return False
        loop += 1
    return True


def prime_sieve(limit):
    prime = [True for _ in range(limit + 1)]
    finalised = []
    p = 2
    while p ** 2 <= limit:
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    for i in range(2, len(prime)):
        if prime[i]:
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
    all_permutations = ["".join(i) for i in list(permutations(string, len(string)))]
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


def is_pandigital(string: str) -> bool:
    if set(string) == set("123456789") and len(string) == len("123456789"):
        return True
    return False
