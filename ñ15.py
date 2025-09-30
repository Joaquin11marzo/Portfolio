def rent(n, i=0):
    if i*i > n:
        return i-1
    return rent(n, i+1)
print(rent(16))
