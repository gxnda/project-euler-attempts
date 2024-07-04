from datetime import datetime

from util import is_prime


def top_right(sl: int) -> int:
    """
    SL 1: 1
    SL 3: 3, 5, 7, 9 +2
    SL 5: 13, 17, 21, 25 +4
    SL 7: 31, 37, 43, 49 +6

    n = (SL + 1) // 2
    SL = 2n - 1

    Top right:
       1, 3, 13, 31 -> n^2 - n + 1 ->(SL ** 2 + 3) // 4
    """
    return (sl ** 2 + 3) // 4


def top_right_is_prime(sl: int) -> bool:
    return is_prime(top_right(sl))


def top_left(sl: int) -> int:
    """
    Top left:
       1, 5, 17, 37 -> 4n^2 - 8n + 5 -> (SL - 1) ** 2 + 1
    """
    return (sl - 1) ** 2 + 1


def top_left_is_prime(sl: int) -> bool:
    return is_prime(top_left(sl))


def bottom_left(sl: int) -> int:
    """
    Bottom left:
    1, 7, 21, 43 -> 4n**2 - 6n + 3 -> SL**2 - SL + 1
    """
    return sl ** 2 - sl + 1


def bottom_left_is_prime(sl: int):
    return is_prime(bottom_left(sl))


def bottom_right_is_prime():
    # Bottom right:
    #   1, 9, 25, 49 ->
    #       1**2, 3**2, 5**2, 7**2 ->
    #           SL**2, never prime.
    return False


def euler_58():
    """
    Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

                                                37 36 35 34 33 32 31
                                                38 17 16 15 14 13 30
                                                39 18  5  4  3 12 29
                                                40 19  6  1  2 11 28
                                                41 20  7  8  9 10 27
                                                42 21 22 23 24 25 26
                                                43 44 45 46 47 48 49

    It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is
    that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 = 62%.

    If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
    If this process is continued, what is the side length of the square spiral for which the ratio of primes along
    both diagonals first falls below 10%?
    """
    side_length = 1
    complete = False
    primes, total = 0, 1
    while not complete:
        total += 4
        side_length += 2
        if top_right_is_prime(side_length):
            primes += 1

        if top_left_is_prime(side_length):
            primes += 1

        if bottom_left_is_prime(side_length):
            primes += 1

        if bottom_right_is_prime():
            primes += 1

        if (primes / total) <= 0.1:
            return side_length


if __name__ == "__main__":
    start = datetime.now()
    print(euler_58())
    end = datetime.now()
    print(end - start)
