def cont_dig(n):
    if n < 10:
        return 1
    return 1 + cont_dig(n//10)

print(cont_dig(123456))
