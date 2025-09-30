def sumhas(n):
    if n == 0:
        return 0
    return n + sumhas(n-1)

print(sumhas(4))
