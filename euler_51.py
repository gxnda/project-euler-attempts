import util


def get_all_prime_wildcard_permutations(wildcard_num: str, prime_sieve: list[int]) -> list[int]:
    perms = []
    if wildcard_num[0] == "*":
        for i in range(1, 9):
            replaced = wildcard_num.replace("*", str(i))
            if int(replaced) in prime_sieve:
                perms.append(int(replaced))

    elif "*" in wildcard_num:
        for i in range(0, 9):
            replaced = wildcard_num.replace("*", str(i))
            if int(replaced) in prime_sieve:
                perms.append(int(replaced))

    else:
        if int(wildcard_num) in prime_sieve:
            perms.append(int(wildcard_num))

    return perms


def get_all_wildcard_permutations(to_be_wildcarded: str):
    length = len(to_be_wildcarded)
    perms = []
    for i in range(2 ** length):
        binary_i = str(bin(i)[2:].zfill(length))

        star_overlay = binary_i.replace("1", "*")
        temp_wildcard_str = to_be_wildcarded
        for j in range(length):
            if star_overlay[j] == "*":
                temp_wildcard_str = temp_wildcard_str[:j] + "*" + temp_wildcard_str[j + 1:]
        perms.append(temp_wildcard_str)

    return perms


def euler_51():
    """
    Prime digit replacements

    Problem 51

    By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine
    possible values: 13, 23, 43, 53, 73, and 83, are all prime.

    By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number
    is the first example having seven primes among the ten generated numbers, yielding the
    family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently, 56003, being
    the first member of this family, is the smallest prime with this property.

    Find the smallest prime which, by replacing part of the number (not necessarily adjacent
    digits) with the same digit, is part of an eight prime value family.
    """
    # test_str = "*3"
    # upper_limit = int(test_str.replace("*", "9")) + 1
    # primes = useful_functions.prime_sieve(upper_limit)
    # print(get_all_prime_wildcard_permutations(test_str, primes))

    primes = useful_functions.prime_sieve(999999)
    print("prime sieve done", len(primes))
    checked = []
    for i in primes:
        if i not in checked:
            all_permutations = get_all_wildcard_permutations(str(i))
            for permutation in all_permutations:
                result = get_all_prime_wildcard_permutations(permutation, primes)
                for j in result:
                    if j not in checked:
                        checked.append(j)
                if len(result) >= 6:
                    print(result)
                if len(result) == 8:
                    return result[0]


if __name__ == "__main__":
    euler_51()
