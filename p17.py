def mosinv(vec, i=0):
    if i < len(vec):
        mosinv(vec, i+1)
        print(vec[i])

mosinv([1, 1, 0, 3, 0, 9])
