def sugeo(n):
    if n == 1:
        return 2
    return -3 * sugeo(n-1)

for i in range(1, 6):
    print(sugeo(i))
