from datetime import datetime
from math import factorial


def euler_53():
    """
    It is not until n = 23, that a value exceed 1 million (23C10 = 1144066)
    How many values of nCr for 1 <= n <= 100 are greater than 1 million?
    """
    total = 0
    for n in range(1, 101):
        for r in range(n + 1):
            result = factorial(n) / ((factorial(r)) * factorial(n-r))
            if result > 1_000_000:
                total += 1
    return total


if __name__ == "__main__":
    start_time = datetime.now()
    print(euler_53())
    end_time = datetime.now()
    print(end_time - start_time)
