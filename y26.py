def es_valido(tablero, fila, col):
    for i in range(fila):
        if tablero[i]==col or abs(tablero[i]-col)==abs(i-fila):
            return False
    return True

def reina(n=8, fila=0, tablero=None):
    if tablero is None:
        tablero=[-1]*n
    if fila==n:
        print(tablero)
        return
    for col in range(n):
        if es_valido(tablero,fila,col):
            tablero[fila]=col
            reina(n,fila+1,tablero)
reina(8)
