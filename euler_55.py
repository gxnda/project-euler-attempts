from datetime import datetime

import util


def reverse_and_add(num):
    return num + int(str(num)[::-1])


def is_lychrel_number(num: int) -> bool:
    attempts = 0
    current_total = num
    while attempts < 50:
        current_total = reverse_and_add(current_total)
        if useful_functions.is_palindromic(str(current_total)):
            return True
        attempts += 1
    return False


def euler_55():
    """
    How many numbers less than 10000 can have their palindromes added to themselves
    """
    count = 0
    for i in range(10000):
        if not is_lychrel_number(i):
            count += 1
    return count


if __name__ == "__main__":
    start = datetime.now()
    print(euler_55())
    end = datetime.now()
    print(end - start)
