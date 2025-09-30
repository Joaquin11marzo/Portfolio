def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        hanoi(n-1, origen, auxiliar, destino)
        print(f"Mover disco {n} de {origen} a {destino}")
        hanoi(n-1, auxiliar, destino, origen)

hanoi(3,"A","C","B")
