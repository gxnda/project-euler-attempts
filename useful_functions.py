

def is_prime(num) -> bool:
    num = abs(num)
    loop = 2
    if num < loop:
        return False
    while loop ** 2 < num + 1:
        if num % loop == 0:
            return False
        loop += 1
    return True


def PrimeSieve(limit):
    # starttime = time()
    prime = [True for i in range(limit + 1)]
    finalised = []
    p = 2
    while p ** 2 <= limit:
        if prime[p] == True:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    for i in range(2, len(prime)):
        if prime[i]:
            finalised.append(i)

    # endtime = time()
    # print((endtime-starttime)*1000)
    return finalised  # returns list
