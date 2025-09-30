def bus_sec(lista, x, i=0):
    if i == len(lista):
        return False
    if lista[i] == x:
        return True
    return bus_sec(lista, x, i+1)

print(bus_sec([1, 1, 0, 3, 0, 9], 0))
