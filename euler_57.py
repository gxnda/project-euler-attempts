"""
It is possible to show that the square root of two can be written as an infinite continued fraction.


sqrt(2) = 1 + 1/(2+(1/(2+1/(2+1/(2...)))))

By expanding this for the first four iterations, we get:
1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 575/408, but the eighth expansion,
1393/985, is the first example where the number of digits in the numerator exceeds
the number of digits in the denominator.

In the first 1000 expansions, how many fractions contain a numerator with
more digits than denominator?
"""

from util import Fraction


def euler_57():
    approx = Fraction(1, 1)
    count = 0
    for i in range(1000):
        approx = (approx + 1).flipped() + 1  # 1.5
        if len(str(approx.numerator)) > len(str(approx.denominator)):
            count += 1

    return count


if __name__ == "__main__":
    print(euler_57())
