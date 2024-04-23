from datetime import datetime


def has_identical_digits(int_1: int, int_2: int) -> bool:
    str_1, str_2 = str(int_1), str(int_2)

    if len(str_1) < len(str_2):  # bolster with 0s
        str_1.zfill(len(str_2) - len(str_1))
    elif len(str_1) > len(str_2):
        str_2.zfill(len(str_1) - len(str_2))

    arr_1 = [i for i in str_1]
    arr_2 = [i for i in str_2]
    return sorted(arr_1) == sorted(arr_2)


def euler_52():
    """
    Permuted Multiples
    Problem 52

    It can be seen that the number, 125874, and its double 251748,
    contain exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
    contain the same digits.
    """
    found = False
    x = 1
    while not found:
        if x % 10000000 == 0:
            print(x)

        if str(x)[0] in ["0", "1"]:
            if has_identical_digits(x, x * 2):
                if has_identical_digits(x, x * 4):
                    if has_identical_digits(x, x * 4):
                        if has_identical_digits(x, x * 5):
                            if has_identical_digits(x, x * 6):
                                return x
        x += 1


if __name__ == "__main__":
    start_time = datetime.now()
    print(euler_52())
    end_time = datetime.now()
    print(end_time - start_time)
