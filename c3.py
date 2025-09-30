def producto(a, b):
    if b == 0:
        return 0
    if b > 0:
        return a + producto(a, b-1)
    return -producto(a, -b)

print(producto(5, 8))