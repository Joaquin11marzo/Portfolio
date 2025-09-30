def pote(b, ex):
    if ex == 0:
        return 1
    return b * pote(b, ex-1)

print(pote(3, 4))
