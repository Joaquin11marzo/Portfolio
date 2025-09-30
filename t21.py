def bus_bin(lista, x, ini=0, fin=None):
    if fin is None:
        fin = len(lista)-1
    if ini > fin:
        return False
    mid = (ini+fin)//2
    if lista[mid] == x:
        return True
    if x < lista[mid]:
        return bus_bin(lista, x, ini, mid-1)
    return bus_bin(lista, x, mid+1, fin)

print(bus_bin([1, 1, 0, 3, 0, 9], 9))
