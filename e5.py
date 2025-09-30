def romdec(rom):
    val = {"I": 1, "V": 5, "X": 10, "L": 50,
               "C": 100, "D": 500, "M": 1000}
    def helper(s, i=0):
        if i == len(s)-1:
            return val[s[i]]
        if val[s[i]] < val[s[i+1]]:
            return -val[s[i]] + helper(s, i+1)
        return val[s[i]] + helper(s, i+1)
    return helper(rom)

print(romdec("XV"))
