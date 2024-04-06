import useful_functions


def reverse_and_add(num):
    return num + int(str(num)[::-1])


def is_Lychrel_number(num: int) -> bool:
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
    How mahy numbers less than 10000 can have their palindoromes added to themselves
    """
    count = 0
    for i in range(10000):
        if is_Lychrel_number(i):
            count += 1
    return count


if __name__ == "__main__":
    print(euler_55())