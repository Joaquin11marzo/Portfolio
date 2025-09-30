def rec_mat(m, f=0, c=0):
    if f == len(m):
        return
    if c < len(m[f]):
        print(m[f][c])
        rec_mat(m, f, c+1)
    else:
        rec_mat(m, f+1, 0)

rec_mat([[1,1],[0,3],[0,9]])
