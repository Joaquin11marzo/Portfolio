def pascal(n, i=0, j=0):
    if j==0 or j==i:
        return 1
    return pascal(n,i-1,j-1)+pascal(n,i-1,j)

for i in range(5):
    fila=[pascal(5,i,j) for j in range(i+1)]
    print(fila)
