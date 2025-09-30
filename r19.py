def suce(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return suce(n-1) + suce(n-2)

print(suce(6))
