def get_digital_sum(num: int):
    return sum([int(i) for i in str(num)])


def euler_56():
    maximum = 0
    for a in range(100):
        for b in range(100):
            res = get_digital_sum(a ** b)
            maximum = max(maximum, res)
    return maximum


if __name__ == "__main__":
    print(euler_56())
