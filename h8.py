def dec_bin(n):
    if n < 2:
        return str(n)
    return dec_bin(n//2) + str(n%2)

print(dec_bin(30))
