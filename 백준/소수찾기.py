def isPrime(num):
    a = 13159
    for i in range(2, num, 1):
        if a % i == 0:
            return 0
        else:
            return 1



isPrime(100)
