import numpy as np
import random
def creacion(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("El valor de n debe ser un número entero positivo.")
    laberinto = np.ones((n, n), dtype=int)
    x, y = 0, 0
    laberinto[x, y] = 0
    while x < n-1 or y < n-1:
        if x == n-1:
            y += 1
        elif y == n-1:
            x += 1
        else:
            if random.choice([True, False]):
                x += 1
            else:
                y += 1
        laberinto[x, y] = 0
    for i in range(n):
        for j in range(n):
            if laberinto[i, j] != 0:
                laberinto[i, j] = random.choice([0, 1])
    return laberinto

def resolver_laberinto(matriz, x=0, y=0, salida=None, visitados=None):
    if salida is None:
        salida = []
    if visitados is None:
        visitados = set()
    if x == len(matriz)-1 and y == len(matriz[0])-1:
        salida.append((x, y))
        return salida
    if x < 0 or x >= len(matriz) or y < 0 or y >= len(matriz[0]) or matriz[x][y] == 1:
        return None
    if (x, y) in visitados:
        return None
    visitados.add((x, y))
    salida.append((x, y))
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        camino = resolver_laberinto(matriz, x+dx, y+dy, salida.copy(), visitados.copy())
        if camino is not None:
            return camino
    return None

def marcar_camino(matriz, camino):
    laberinto_marcado = matriz.copy().astype(str)
    laberinto_marcado[laberinto_marcado == "1"] = "█"
    laberinto_marcado[laberinto_marcado == "0"] = " "
    if camino:
        for (x, y) in camino:
            laberinto_marcado[x][y] = "*"
    return laberinto_marcado

n = 10
lab = creacion(n)
camino = resolver_laberinto(lab)

print("Laberinto generado:")
print(lab, "\n")
print("Camino encontrado:", camino, "\n")

if camino:
    print("Laberinto con el camino marcado:")
    print("\n".join(" ".join(f"{c}" for c in fila) for fila in marcar_camino(lab, camino)))
else:
    print("No se encontró salida.")
