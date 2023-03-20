"""
All solutions to my project Euler questions so far.
Some of this code is absolutely appalling because it was made literally after
I finished snakify.org, so I knew nothing about variable naming et cetera.

- Gabriel Lancaster-West
"""

from useful_functions import *
from math import sqrt, factorial, ceil, floor
from time import time


def euler_1():
    """Multiples of 3 or 5"""
    length, total = 1000, 0
    for i in range(length):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    print(total)


def euler_2():
    result = 0
    count = 0
    i = 1
    while result < 4000000:
        a = 0
        b = 1
        if i == 0:
            a = 0
            b = 0
        for j in range(i - 1):
            c = a
            a = b + a
            b = c
            result = a + b
        if result % 2 == 0:
            count += result
        i += 1

    print(count)


def euler_3():
    i, n = 1, 600851475143
    while i * i <= n:
        if n % i == 0:
            n = n // i
        i += 1
    print(n)


def euler_4():
    palindrome = 0
    for j in range(700, 999):
        for k in range(700, 999):
            if str(j * k) == str(j * k)[::-1] and j * k >= palindrome:
                palindrome = j * k
    print(palindrome)


def euler_5():

    primes = []
    for i in range(20):
        if is_prime(i) and i > 1:
            primes.append(i)

    # finds prime factors of numbers 1 to 20
    factors, temp = [], []
    for number in range(20):
        while number > 1:
            for i in range(len(primes)):
                if number % primes[i] == 0:
                    number = number // primes[i]
                    temp.append(primes[i])
        if not temp:
            temp = [1]
        factors.append(temp)
        temp = []

    # finds how often each letter comes up per number
    freq = [1] * 20
    for i in range(len(factors)):
        length_of_sublists = len(factors[i])
        for j in range(length_of_sublists):
            temp_freq = [1] * 20
            for count in factors[i]:
                temp_freq[count] *= count
                if temp_freq[count] > freq[count]:
                    freq[count] = temp_freq[count]
    total = 1
    for i in range(len(freq)):
        total *= freq[i]
    print(total)


def euler_6():
    sumsqr, total = 0, 0
    for i in range(1, 101):
        sumsqr += i * i
        total += i
    print((total * total) - sumsqr)


def euler_7():
    count = 0
    i = 1
    while count < 10002:
        if is_prime(i):
            count += 1
        if count == 10002:
            print(i)
        i += 1


def euler_8():
    longboi = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    splitted = [char for char in longboi]
    product = 1
    greatest = 0
    for i in range(len(splitted) - 13):
        for j in range(1, 14):
            product *= int(splitted[i - 1 + j])
        if product > greatest:
            greatest = product
        product = 1
    print("Greatest is", greatest)


def euler_9():
    for i in range(500):
        for j in range(500):
            if sqrt(i * i + j * j) % 1 == 0:
                if i + j + int(sqrt(i * i + j * j)) == 1000 and i > j:
                    print(int(i * j * sqrt(i * i + j * j)))


def euler_10():
    total = 0
    for i in range(2, 2000000):
        if is_prime(i):
            total += i
    print(total)


def euler_11():

    def grid():
        return [[
            '08', '02', '22', '97', '38', '15', '00', '40', '00', '75', '04',
            '05', '07', '78', '52', '12', '50', '77', '91', '08'
        ],
                [
                    '49', '49', '99', '40', '17', '81', '18', '57', '60', '87',
                    '17', '40', '98', '43', '69', '48', '04', '56', '62', '00'
                ],
                [
                    '81', '49', '31', '73', '55', '79', '14', '29', '93', '71',
                    '40', '67', '53', '88', '30', '03', '49', '13', '36', '65'
                ],
                [
                    '52', '70', '95', '23', '04', '60', '11', '42', '69', '24',
                    '68', '56', '01', '32', '56', '71', '37', '02', '36', '91'
                ],
                [
                    '22', '31', '16', '71', '51', '67', '63', '89', '41', '92',
                    '36', '54', '22', '40', '40', '28', '66', '33', '13', '80'
                ],
                [
                    '24', '47', '32', '60', '99', '03', '45', '02', '44', '75',
                    '33', '53', '78', '36', '84', '20', '35', '17', '12', '50'
                ],
                [
                    '32', '98', '81', '28', '64', '23', '67', '10', '26', '38',
                    '40', '67', '59', '54', '70', '66', '18', '38', '64', '70'
                ],
                [
                    '67', '26', '20', '68', '02', '62', '12', '20', '95', '63',
                    '94', '39', '63', '08', '40', '91', '66', '49', '94', '21'
                ],
                [
                    '24', '55', '58', '05', '66', '73', '99', '26', '97', '17',
                    '78', '78', '96', '83', '14', '88', '34', '89', '63', '72'
                ],
                [
                    '21', '36', '23', '09', '75', '00', '76', '44', '20', '45',
                    '35', '14', '00', '61', '33', '97', '34', '31', '33', '95'
                ],
                [
                    '78', '17', '53', '28', '22', '75', '31', '67', '15', '94',
                    '03', '80', '04', '62', '16', '14', '09', '53', '56', '92'
                ],
                [
                    '16', '39', '05', '42', '96', '35', '31', '47', '55', '58',
                    '88', '24', '00', '17', '54', '24', '36', '29', '85', '57'
                ],
                [
                    '86', '56', '00', '48', '35', '71', '89', '07', '05', '44',
                    '44', '37', '44', '60', '21', '58', '51', '54', '17', '58'
                ],
                [
                    '19', '80', '81', '68', '05', '94', '47', '69', '28', '73',
                    '92', '13', '86', '52', '17', '77', '04', '89', '55', '40'
                ],
                [
                    '04', '52', '08', '83', '97', '35', '99', '16', '07', '97',
                    '57', '32', '16', '26', '26', '79', '33', '27', '98', '66'
                ],
                [
                    '88', '36', '68', '87', '57', '62', '20', '72', '03', '46',
                    '33', '67', '46', '55', '12', '32', '63', '93', '53', '69'
                ],
                [
                    '04', '42', '16', '73', '38', '25', '39', '11', '24', '94',
                    '72', '18', '08', '46', '29', '32', '40', '62', '76', '36'
                ],
                [
                    '20', '69', '36', '41', '72', '30', '23', '88', '34', '62',
                    '99', '69', '82', '67', '59', '85', '74', '04', '36', '16'
                ],
                [
                    '20', '73', '35', '29', '78', '31', '90', '01', '74', '31',
                    '49', '71', '48', '86', '81', '16', '23', '57', '05', '54'
                ],
                [
                    '01', '70', '54', '71', '83', '51', '54', '69', '16', '92',
                    '33', '48', '61', '43', '52', '01', '89', '19', '67', '48'
                ]]

    grid = grid()

    def HorizVert(grid_horiz_vert):
        biggestx = 1
        biggesty = 1
        # horizontal
        for i in range(len(grid_horiz_vert)):
            for j in range(0, len(grid_horiz_vert[0])):
                try:
                    sumx = int(grid_horiz_vert[i][j]) * int(
                        grid_horiz_vert[i][j + 1]) * int(
                            grid_horiz_vert[i][j + 2]) * int(
                                grid_horiz_vert[i][j + 3])
                    if sumx > biggestx:
                        biggestx = sumx
                except KeyError:
                    pass
        for i in range(len(grid_horiz_vert)):
            for j in range(0, len(grid_horiz_vert[0])):
                try:
                    sumy = int(grid_horiz_vert[j][i]) * int(
                        grid_horiz_vert[j][i + 1]) * int(
                            grid_horiz_vert[j][i + 2]) * int(
                                grid_horiz_vert[i][i + 3])
                    if sumy > biggesty:
                        biggesty = sumy
                except KeyError:
                    pass
        return biggestx, biggesty

    def Diagonal(grid_diagonal):
        b1, b2, b3, b4 = 1, 1, 1, 1
        for j in range(len(grid_diagonal)):
            for i in range(len(grid_diagonal)):
                try:
                    # goes horizontally across
                    a = int(grid_diagonal[i + j][len(grid_diagonal) - i])
                    b = int(grid_diagonal[i + j + 1][len(grid_diagonal) - i -
                                                     1])
                    c = int(grid_diagonal[i + j + 2][len(grid_diagonal) - i -
                                                     2])
                    d = int(grid_diagonal[i + j + 3][len(grid_diagonal) - i -
                                                     3])
                    product = a * b * c * d
                    if product > b4:
                        b4 = product

                except IndexError:
                    pass
                try:
                    # goes vertically down
                    a = int(grid_diagonal[i + j][len(grid_diagonal) - i])
                    b = int(grid_diagonal[i + j + 1][len(grid_diagonal) - i -
                                                     1])
                    c = int(grid_diagonal[i + j + 2][len(grid_diagonal) - i -
                                                     2])
                    d = int(grid_diagonal[i + j + 3][len(grid_diagonal) - i -
                                                     3])
                    product = a * b * c * d
                    if product > b1:
                        b1 = product
                except IndexError:
                    pass

                try:
                    # goes horizontally across
                    a = int(grid_diagonal[i][len(grid_diagonal) - i - j])
                    b = int(grid_diagonal[i - 1][len(grid_diagonal) - i - j -
                                                 1])
                    c = int(grid_diagonal[i - 2][len(grid_diagonal) - i - j -
                                                 2])
                    d = int(grid_diagonal[i - 3][len(grid_diagonal) - i - j -
                                                 3])
                    product = a * b * c * d
                    if product > b2:
                        b2 = product

                except IndexError:
                    pass
                try:
                    # goes vertically down
                    a = int(grid_diagonal[i + j][len(grid_diagonal) - i])
                    b = int(grid_diagonal[i + j + 1][len(grid_diagonal) - i -
                                                     1])

                    c = int(grid_diagonal[i + j + 2][len(grid_diagonal) - i -
                                                     2])
                    d = int(grid_diagonal[i + j + 3][len(grid_diagonal) - i -
                                                     3])
                    product = a * b * c * d
                    if product > b3:
                        b3 = product

                except IndexError:
                    pass
        return b4, b1, b2, b3

    print(Diagonal(grid))
    print(HorizVert(grid))

    # [horizontal(grid_horiz_vert, run_len), vertical(grid_horiz_vert, run_len),diagonal_natural(grid_horiz_vert, run_len), diagonal_reverse(grid_horiz_vert, run_len)]
    # [48477312, 51267216, 40304286, 70600674]


def euler_12():

    def factors(x):
        result = []
        i = 1
        while i * i <= x:
            if x % i == 0:
                result.append(i)
                if x // i != i:
                    result.append(x // i)
            i += 1
        return result

    print(factors(500))


def euler_13():
    with open("numbers.txt") as file:
        numbers = (file.read()).split("\n")
        total = 0
        for val in numbers:
            val = int(val)
            total += val
        print(total)


def euler_14():
    maxcount = 0
    for n in range(1, 1000000, 2):
        original = n
        count = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                count += 1
            else:
                n = 3 * n + 1
                count += 1
        if count > maxcount:
            maxcount = count
            print(maxcount, original)


def euler_15():
    print(factorial(40) // (factorial(40 - 20) * factorial(20)))


def euler_16():
    num = str(2**1000)
    total = 0
    for char in num:
        total += int(char)
    print(total)


def euler_17():
    units = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine"
    ]
    tens = [
        "",
        "ten",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    teens = [
        "", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]

    total = len("onethousand")
    for i in range(1, 1000):
        word = ""
        if i >= 100:
            word += units[int(str(i)[-3])]
            word += "hundred"
            if int(str(i)[-2]) != 0 or int(str(i)[-1]) != 0:
                word += "and"

        if i >= 10:
            if int(str(i)[-2]) == 1 and int(
                    str(i)[-1]) != 0:  # if its in the teens
                word += teens[int(str(i)[-1])]  # adds the appropriate number
            else:
                word += tens[int(str(i)[-2])]
        try:
            if int(str(i)[-2]) >= 2 or int(str(i)[-2]) < 1:
                word += units[int(str(i)[-1])]
        except KeyError:
            word += units[int(str(i)[-1])]
        total += len(word)
        print(word)
    print(total)


def euler_18():

    def GenerateTriangle():
        with open("triangle.txt", "rt") as file:
            triangle = (file.read()).split("\n")
        for i in range(len(triangle)):
            # noinspection PyTypeChecker
            triangle[i] = triangle[i].split(" ")
            print(triangle[i])
        return triangle

    def FindPairBelow(triangle, row, index):
        if row > 1:
            if 0 <= index < len(triangle[-(row - 1)]):
                right = triangle[-(row - 1)][index]
            else:
                right = 0
            if index <= len(triangle[-(row - 1)]):
                left = triangle[-(row - 1)][index + 1]
            else:
                left = 0
            return [int(left), int(right)]
        else:
            return [0, 0]

    def AppendMaxPairs(triangle):
        newtriangle = triangle
        for rows in range(1, len(newtriangle) + 1):
            reverserows = -rows
            for index in range(len(newtriangle[reverserows])):
                left, right = FindPairBelow(triangle, rows, index)

                if left > right:
                    newtriangle[reverserows][index] = str(
                        int(newtriangle[reverserows][index]) + int(left))
                    # print("adding", left, "to get", newtriangle[reverserows][index], "L")
                elif right >= left:
                    newtriangle[reverserows][index] = str(
                        int(newtriangle[reverserows][index]) + int(right))
                    # print("adding", right, "to get", newtriangle[reverserows][index], "R")
                else:
                    print("how have you messed that up")

            if -(rows - 1) < 0:
                newtriangle[-(rows - 1)] = []
                for i in range(len(newtriangle)):
                    if newtriangle[i]:
                        print(newtriangle[i])

    arr = GenerateTriangle()
    AppendMaxPairs(arr)


def euler_19():
    pass  # I did do it, but it must've been at school


def euler_20():
    n = 100
    total = 1
    for i in range(1, n + 1):
        total *= i
    total = str(total)
    # total = 0
    for char in total:
        total += int(char)
    print(total)


def euler_21():

    def FindPrimeProducts(num, prime_sieve_var):
        prime_sieve_var = prime_sieve_var[:num]
        # loop through prime_sieve_var, if % = 0 then its a factor
        factors = []
        for i in range(1, len(prime_sieve_var)):
            if num % i == 0:
                factors.append(i)
        return factors

    sieve = prime_sieve(10000)
    total = 0

    def SumOfList(arr):
        total_sum_of_list = 0
        for val in arr:
            total_sum_of_list += val
        return total_sum_of_list

    for a in range(1, 10000):  # a
        B = SumOfList(FindPrimeProducts(a, sieve))
        DB = SumOfList(FindPrimeProducts(B, sieve))
        if DB == a and B != a:
            print("y")
            print(B, a)
            total += B + a

    print(total)
    # d(a) = b and d(b) = a


def euler_22():
    names = sorted((open("names.txt", "rt").read()).split(","))
    total = 1
    for i in range(len(names)):
        print(names[i])
        namesum = 0
        for length in range(len(names[i])):
            convertedchar = ord(str(names[i][length]))
            namesum += convertedchar - 64
        total += namesum
    print(total)


def euler_23():

    starttime = time()

    def IsAbundant(n):
        divisor_sum = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisor_sum += i
                if i != n // i:
                    divisor_sum += n // i
        return divisor_sum > n

    abundant = [i for i in range(1, 28124) if IsAbundant(i)]

    NotSum = set(range(1, 28124))
    for i in abundant:
        for j in abundant:
            if i + j < 28124:
                NotSum.discard(i + j)
    endtime = time()
    print(endtime - starttime)
    print(sum(NotSum))
    # 28 seconds lets gooooooo


def euler_24():
    start_time = time()
    val = 1000000 - 1
    num = 9
    arr = [i for i in range(10)]
    order = str()
    while num != -1:
        multiple = floor(val / factorial(num))
        val = val - factorial(num) * multiple
        order += str(arr[multiple])
        arr.pop(multiple)
        num -= 1
    end_time = time()
    print((end_time - start_time) * 1000)
    print(order)


def euler_25():

    def Fibonacci(n):
        return int(
            round((((1 + sqrt(5)) / 2)**n - ((1 - sqrt(5)) / 2)**n) // sqrt(5),
                  0))

    freq = dict()
    for i in range(2000):
        length = len(str(Fibonacci(i)))
        if length not in freq:
            freq[length] = 1
            # print("("+str(length)+","+str(i)+")")
            # print("y-0\\ =\\ \\frac{"+str(i)+"-0}{"+str(length)+"-1}\\left(x-1\\right)")
            if length > 1:
                print("(" + str(i) + "," + str((i - 0) / (length - 1)) + ")")
            else:
                print("teeny weeny")
        else:
            freq[length] += 1
    # for val in freq:
    #  print("("+str(val) + "," + str(freq[val]) + ")")
    "y-0\\ =\\ \\frac{7-0}{2-1}\\left(x-1\\right)"

    # solved on desmos and wolfram alpha


def euler_26():

    def BusStop(digit, div):
        # assuming div > 1 and an integer
        result = str()
        allDigits = []
        NotRepeated = True
        count = 0
        while NotRepeated:
            result += str(digit // div)
            carry = digit - (div * (digit // div))
            digit = carry * 10
            if digit in allDigits:
                # print(result[0]+"."+result[1:], digit, count, div)
                return [result[0] + "." + result[1:], digit, count, div]
            else:
                allDigits.append(digit)
            count += 1

    maxrepeat = 0
    maxnum = 0
    for i in range(2, 1000):
        num = BusStop(1, i)[2]
        if num > maxrepeat:
            maxrepeat = num
            maxnum = i
    print("Answer is:", maxnum, "\nWith a repeating part of:", maxrepeat)
    print("\n\nRaw Output:\n\n")
    print(BusStop(1, maxnum)[0])
    # answer is 983


def euler_27():

    def CycleLength(b2, c2):
        Complete = False
        total = 0
        x = 0
        while not Complete:
            if not is_prime(x**2 + b2 * x + c2):  # if number isn't prime
                Complete = True  # end cycle and return count
            else:
                total += 1
                x += 1
        return total

    AllNumbers = prime_sieve(1001)
    longest = 0
    best_b, best_c = None, None
    for val1 in AllNumbers:
        print(val1)  # progress bar
        for val2 in AllNumbers:
            for b in [val1, -1 * val1]:
                for c in [val2, -1 * val2]:
                    count = CycleLength(b, c)
                    if count > longest:
                        print(count)
                        longest = count
                        best_b, best_c = b, c
    print(best_b, best_c, longest)


def euler_28():
    total = 1
    for sidelength in range(2, 1002):
        total += 2 * (sidelength**2) - sidelength + 1.5
    print(ceil(total))


def euler_29():
    a = [val for val in range(2, 101)]
    results = set()
    for val1 in a:
        for val2 in a:
            results.add(val1**val2)
    print(len(results))


def euler_30():

    def CheckSumOfFifthDigits(num_inner):
        num_inner = str(num_inner)
        total_inner = 0
        for digit in num_inner:
            total_inner += int(digit)**5
        if total_inner == int(num_inner):
            return True
        else:
            return False

    starttime = time()
    works = []
    AllNum = [str(i) for i in range(2, ((9**5) * 6) + 1)]
    for num in AllNum:
        if CheckSumOfFifthDigits(num):
            works.append(num)
    print(works)
    total = 0
    for val in works:
        val = int(val)
        total += val
    endtime = time()
    print(endtime - starttime)
    print(total)


def euler_31():
    """Have a different for loop for each coin"""
    max_count = 200
    numPaths = 0
    for one in range(max_count // 1 + 1):
        print(one)
        for two in range(max_count // 2 + 1):
            if one + two * 2 <= 200:
                for five in range(max_count // 5 + 1):
                    if one + two * 2 + five * 5 <= 200:
                        for ten in range(max_count // 10 + 1):
                            if one + two * 2 + five * 5 + ten * 10 <= 200:
                                for twenty in range(max_count // 20 + 1):
                                    if one + two * 2 + five * 5 + ten * 10 + twenty * 20 <= 200:
                                        for fifty in range(max_count // 50 +
                                                           1):
                                            if one + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty * 50 <= 200:
                                                for quid in range(max_count //
                                                                  100 + 1):
                                                    if one + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty * 50 + quid * 100 <= 200:
                                                        for twoQuid in range(
                                                                max_count //
                                                                200 + 1):
                                                            if one * 1 + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty * 50 + quid * 100 + twoQuid * 200 == 200:
                                                                numPaths += 1
    print(numPaths)


def euler_32():
    """
    Pandigital products

    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for
    example, the 5-digit number, 15234, is 1 through 5 pandigital. The product 7254 is unusual, as the identity,
    39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
    """
    all_4_digits = [i for i in range(1000, 10000)]
    all_prime_factors = [get_factors_dict(i) for i in all_4_digits]
    products_that_work = set()
    for i in range(len(all_4_digits)):
        for key in list(all_prime_factors[i].keys()):
            all_combined = str(all_4_digits[i]) + str(key) + str(
                all_prime_factors[i][key])
            if is_pandigital(all_combined):
                print(
                    f"{key} * {all_prime_factors[i][key]} = {all_4_digits[i]}")
                products_that_work.add(all_4_digits[i])
    return sum(products_that_work)


def euler_33():
    """
    Digit cancelling fractions

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
    incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples. There are exactly four non-trivial examples
    of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
    """
    all_2_digits = [i for i in range(10, 100)]
    fractions = []
    for num in range(len(all_2_digits) - 1):
        for den in range(len(all_2_digits)):
            if den > num:
                fractions.append([all_2_digits[num], all_2_digits[den]])

    valid_simplifications = []
    for fraction in fractions:
        numerator = str(fraction[0])
        denominator = str(fraction[1])
        if (numerator[0] != numerator[1]) and (
                denominator[0] !=
                denominator[1]) and set(numerator) & set(denominator):
            shared_digits = list(set(numerator) & set(denominator))
            for shared in shared_digits:
                new_num = numerator.strip(shared)
                new_den = denominator.strip(shared)
                zeros_in_both_original = "0" in numerator and "0" in denominator
                if int(new_num) < int(new_den) and "0" not in [
                        new_num, new_den
                ] and not zeros_in_both_original:
                    if int(numerator) / int(denominator) == int(new_num) / int(
                            new_den):
                        # print(new_num, "/", new_den, ",", numerator, "/", denominator)
                        valid_simplifications.append([new_num, new_den])

    numerator_product, denominator_product = 1, 1
    for fraction in valid_simplifications:
        numerator_product *= int(fraction[0])
        denominator_product *= int(fraction[1])
    # factors_numerator = get_factors(numerator_product)
    # factors_denominator = get_factors(denominator_product)
    print(numerator_product, "/", denominator_product)
    # Outputs 8/800, this is trivial enough to be simplified by hand to give an answer of 1/100.
    # ALSO RAPID (like 0.004s kinda speedy)


def euler_34():
    # biggest is 7 digits because highest number possible is 2540160 (7 * 9!)

    def IsDigitFactorial(num_inner):
        if len(str(num_inner)) == 1:
            return False
        else:
            num_inner = int(num_inner)
            arr = [i for i in str(num_inner)]
            total = 0
            for val in arr:
                if total <= num_inner:
                    total += factorial(int(val))
                else:
                    return False
            if total == num_inner:
                return True
            else:
                return False

    count = 0
    for num in range(0, 2540161):
        if IsDigitFactorial(num):
            count += num
            print(count)


def euler_35():

    def is_circular_prime(num: int) -> bool:
        all_permutations = [int(j) for j in get_all_rotations(str(num))]
        for num in all_permutations:
            if not is_prime(num):
                return False
        return True

    count = 0
    primes = prime_sieve(1_000_000)
    for i in primes:
        if is_circular_prime(i):
            count += 1
    return count  # runs in 2.89s, answer = 55


def euler_36():

    def IsPalindromic(num):
        num = str(num)
        reversed_num = num[::-1]
        if num == reversed_num:
            return True
        else:
            return False

    total = 0
    for i in range(1, 1000001):
        if IsPalindromic(i) and IsPalindromic(str(bin(i))[2:]):
            total += i

    print(total)


def euler_37():
    """
    Truncatable primes

    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
    left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly, we can work from right to left:
    3797, 379, 37, and 3.
    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    """

    def is_prime_as_truncate_l_to_r(string: str) -> bool:
        while len(string) > 1:
            string = string[1:]
            if not is_prime(int(string)):
                return False
        return True

    def is_prime_as_truncate_r_to_l(string: str) -> bool:
        while len(string) > 1:
            string = string[:-1]
            if not is_prime(int(string)):
                return False
        return True

    number_found = 0
    found = set()
    n = 10
    while number_found < 11:
        if is_prime_as_truncate_l_to_r(str(n)) and is_prime_as_truncate_r_to_l(
                str(n)) and is_prime(n):
            print(n)
            found.add(n)
            number_found += 1
        n += 1
    return sum(found)
    # 748317 in 2.313sec


def euler_38():
    """
    Pandigital multiples
    Problem 38
    Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
    By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated
    product of 192 and (1,2,3).
    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
    which is the concatenated product of 9 and (1,2,3,4,5).
    What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
    with (1,2, ... , n) where n > 1?
    """
    all_pandigital = set()
    for i in range(1, 10000):
        num = ""
        n = 1
        while len(num) <= len("123456789"):
            num += str(i * n)
            if n > 1 and is_pandigital(num):
                all_pandigital.add(num)
            n += 1
    # that was easier than i thought
    return max(all_pandigital)  # 932718654 in 0.0219s


def euler_39():
    """
    Integer right triangles
    Problem 39
    If p is the perimeter of a right angle triangle with integral length sides, 
    {a,b,c}, there are exactly three solutions for p = 120.
    {20,48,52}, {24,45,51}, {30,40,50}
    For which value of p ≤ 1000, is the number of solutions maximised?

    note: for any integers a & b, sides a^2 - b^2 and 2ab create integer side length a^2 + b^2
    """
    max_count = 0
    max_p = 0
    all_triples = generate_pythagorean_triples(1000)
    for p in range(1001):
        count = 0
        for triple in all_triples:
            if sum(triple) == p:
                count += 1
        if count > max_count:
            max_count = count
            max_p = p
    return max_p
    # 840
    # 0.190s


def euler_40():
    """
    Champernowne's constant
    Problem 40
    An irrational decimal fraction is created by concatenating the positive integers:
    0.123456789101112131415161718192021...
    It can be seen that the 12th digit of the fractional part is 1.
    If dn represents the nth digit of the fractional part, 
    find the value of the following expression.
    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
    """
    # generate the whole thing
    const = str()
    num_to_add = 1
    while len(const) <= 1000000:
        const += str(num_to_add)
        num_to_add += 1

    def d(index):
        return int(const[index - 1])
    
    return d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)
    #210
    #0.13741087913513184


def euler_41():
    n = 2142
    while True:
        if is_prime(n) and is_pandigital(n):
            print(n)
        n += 1


if __name__ == "__main__":
    start = time()
    print(euler_41())
    end = time()
    print(end - start)


#for thing in range(1, length+1):
#            comp += str(thing)
#        if is_pandigital(str(i), comp) and is_prime(i):
#            print(i)
#
#

