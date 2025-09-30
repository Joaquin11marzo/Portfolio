def inv_num(n, inv=0):
    if n == 0:
        return inv
    return inv_num(n//10, inv*10 + n%10)

print(inv_num(12345))
