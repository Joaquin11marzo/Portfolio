def sumdig(n):
    if n == 0:
        return 0
    return n%10 + sumdig(n//10)

print(sumdig(11032009))
