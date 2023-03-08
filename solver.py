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
    temp_freq = [1] * 20
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
    sumsqr, sum = 0, 0
    for i in range(1, 101):
        sumsqr += i * i
        sum += i
    print((sum * sum) - sumsqr)


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
    sum = 0
    for i in range(2, 2000000):
        if is_prime(i):
            sum += i
    print(sum)


def euler_11():
    def grid():
        return [[
            '08', '02', '22', '97', '38', '15', '00', '40', '00', '75', '04', '05',
            '07', '78', '52', '12', '50', '77', '91', '08'
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

    def HorizVert(grid):
        biggestx = 1
        biggesty = 1
        # horizontal
        for i in range(len(grid)):
            for j in range(0, len(grid[0])):
                try:
                    sumx = int(grid[i][j]) * int(grid[i][j + 1]) * int(
                        grid[i][j + 2]) * int(grid[i][j + 3])
                    if sumx > biggestx:
                        biggestx = sumx
                except:
                    pass
        for i in range(len(grid)):
            for j in range(0, len(grid[0])):
                try:
                    sumy = int(grid[j][i]) * int(grid[j][i + 1]) * int(
                        grid[j][i + 2]) * int(grid[i][i + 3])
                    if sumy > biggesty:
                        biggesty = sumy
                except:
                    pass
        return biggestx, biggesty

    def Diagonal(grid):
        b1, b2, b3, b4 = 1, 1, 1, 1
        for j in range(len(grid)):
            for i in range(len(grid)):
                try:
                    # goes horizontally across
                    a = int(grid[i + j][len(grid) - i])
                    b = int(grid[i + j + 1][len(grid) - i - 1])
                    c = int(grid[i + j + 2][len(grid) - i - 2])
                    d = int(grid[i + j + 3][len(grid) - i - 3])
                    product = a * b * c * d
                    if product > b4:
                        b4 = product

                except IndexError:
                    pass
                try:
                    # goes vertically down
                    a = int(grid[i + j][len(grid) - i])
                    b = int(grid[i + j + 1][len(grid) - i - 1])
                    c = int(grid[i + j + 2][len(grid) - i - 2])
                    d = int(grid[i + j + 3][len(grid) - i - 3])
                    product = a * b * c * d
                    if product > b1:
                        b1 = product
                except IndexError:
                    pass

                try:
                    # goes horizontally across
                    a = int(grid[i][len(grid) - i - j])
                    b = int(grid[i - 1][len(grid) - i - j - 1])
                    c = int(grid[i - 2][len(grid) - i - j - 2])
                    d = int(grid[i - 3][len(grid) - i - j - 3])
                    product = a * b * c * d
                    if product > b2:
                        b2 = product

                except IndexError:
                    pass
                try:
                    # goes vertically down
                    a = int(grid[i + j][len(grid) - i])
                    b = int(grid[i + j + 1][len(grid) - i - 1])

                    c = int(grid[i + j + 2][len(grid) - i - 2])
                    d = int(grid[i + j + 3][len(grid) - i - 3])
                    product = a * b * c * d
                    if product > b3:
                        b3 = product

                except IndexError:
                    pass
        return b4, b1, b2, b3

    print(Diagonal(grid))
    print(HorizVert(grid))

    # [horizontal(grid, run_len), vertical(grid, run_len),diagonal_natural(grid, run_len), diagonal_reverse(grid, run_len)]
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
        sum = 0
        for val in numbers:
            val = int(val)
            sum += val
        print(sum)


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
    num = str(2 ** 1000)
    sum = 0
    for char in num:
        sum += int(char)
    print(sum)


def euler_17():
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", ]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    total = len("onethousand")
    for i in range(1, 1000):
        word = ""
        if i >= 100:
            word += units[int(str(i)[-3])]
            word += "hundred"
            if int(str(i)[-2]) != 0 or int(str(i)[-1]) != 0:
                word += "and"

        if i >= 10:
            if int(str(i)[-2]) == 1 and int(str(i)[-1]) != 0:  # if its in the teens
                word += teens[int(str(i)[-1])]  # adds the appropriate number



            else:
                word += tens[int(str(i)[-2])]
        try:
            if int(str(i)[-2]) >= 2 or int(str(i)[-2]) < 1:
                word += units[int(str(i)[-1])]
        except:
            word += units[int(str(i)[-1])]
        total += len(word)
        print(word)
    print(total)


def euler_18():
    def GenerateTriangle():
        with open("triangle.txt", "rt") as file:
            triangle = (file.read()).split("\n")
        for i in range(len(triangle)):
            triangle[i] = triangle[i].split(" ")
            print(triangle[i])
        return triangle

    def FindPairBelow(triangle, row, index):
        if row > 1:
            if index >= 0 and index < len(triangle[-(row - 1)]):
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
            reverserows = -(rows)
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
                    if newtriangle[i] != []:
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
    sum = 0
    for char in total:
        sum += int(char)
    print(sum)


def euler_21():
    def primesieve(limit):
        starttime = time()
        prime = [True for i in range(limit + 1)]
        finalised = []
        p = 2
        while p ** 2 <= limit:
            if prime[p] == True:
                for i in range(p * p, limit + 1, p):
                    prime[i] = False
            p += 1
        return prime

        endtime = time()

    def FindPrimeProducts(num, sieve):
        sieve = sieve[:num]
        # loop through sieve, if % = 0 then its a factor
        factors = []
        for i in range(1, len(sieve)):
            if num % i == 0:
                factors.append(i)
        return factors

    sieve = primesieve(10000)
    total = 0

    def SumOfList(list):
        total = 0
        for val in list:
            total += val
        return total

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
        for i in range(2, int(n ** 0.5) + 1):
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
    starttime = time()
    val = 1000000 - 1
    num = 9
    list = [i for i in range(10)]
    order = str()
    while num != -1:
        multiple = floor(val / factorial(num))
        val = val - factorial(num) * multiple
        order += str(list[multiple])
        list.pop(multiple)
        num -= 1
    endtime = time()
    print(endtime - starttime) * 1000
    print(order)


def euler_25():
    def Fibonacci(n):
        return int(round((((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) // sqrt(5), 0))

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
                NotRepeated = False
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
    def CycleLength(b, c):
        Complete = False
        count = 0
        x = 0
        while not Complete:
            if not is_prime(x ** 2 + b * x + c):  # if number isn't prime
                Complete = True  # end cycle and return count
            else:
                count += 1
                x += 1
        return count

    AllNumbers = PrimeSieve(1001)
    longest = 0
    bestb, bestc = None, None
    for val1 in AllNumbers:
        print(val1)  # progress bar
        for val2 in AllNumbers:
            for b in [val1, -1 * val1]:
                for c in [val2, -1 * val2]:
                    count = CycleLength(b, c)
                    if count > longest:
                        print(count)
                        longest = count
                        bestb, bestc = b, c
    print(bestb, bestc, longest)


def euler_28():
    sum = 1
    for sidelength in range(2, 1002):
        sum += 2 * (sidelength ** 2) - sidelength + 1.5
    print(ceil(sum))


def euler_29():
    a = [val for val in range(2, 101)]
    results = set()
    for val1 in a:
        for val2 in a:
            results.add(val1 ** val2)
    print(len(results))


def euler_30():
    def CheckSumOfFifthDigits(num):
        num = str(num)
        total = 0
        for digit in num:
            total += int(digit) ** 5
        if total == int(num):
            return True
        else:
            return False

    starttime = time()
    works = []
    AllNum = [str(i) for i in range(2, ((9 ** 5) * 6) + 1)]
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
    start = time()
    max = 200
    numPaths = 0
    for one in range(max // 1 + 1):
        print(one)
        for two in range(max // 2 + 1):
            if one + two * 2 <= 200:
                for five in range(max // 5 + 1):
                    if one + two * 2 + five * 5 <= 200:
                        for ten in range(max // 10 + 1):
                            if one + two * 2 + five * 5 + ten * 10 <= 200:
                                for twenty in range(max // 20 + 1):
                                    if one + two * 2 + five * 5 + ten * 10 + twenty * 20 <= 200:
                                        for fifty in range(max // 50 + 1):
                                            if one + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty * 50 <= 200:
                                                for quid in range(max // 100 + 1):
                                                    if one + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty * 50 + quid * 100 <= 200:
                                                        for twoQuid in range(max // 200 + 1):
                                                            if one * 1 + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty * 50 + quid * 100 + twoQuid * 200 == 200:
                                                                numPaths += 1

    end = time()
    print(end - start)
    print(numPaths)


def euler_32():
    """Pandigital products"""
    pass