def inv_cad(cad):
    if cad == "":
        return ""
    return cad[-1] + inv_cad(cad[:-1])

print(inv_cad("nacho"))
