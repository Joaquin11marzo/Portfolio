def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

def mcm(a, b):
    return abs(a*b) // mcd(a, b)

print(mcm(12, 18))
