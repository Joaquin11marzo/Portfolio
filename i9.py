def logente(n, b):
    if n < b:
        return 0
    return 1 + logente(n//b, b)

print(logente(25, 5))
