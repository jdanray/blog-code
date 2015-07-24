import copy

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def langford(n, string):
    if n == 0:
        return [string]

    solutions = []
    for i in range(len(string) - n - 1):
        if string[i] == None and string[i + n + 1] == None:
            s = copy.copy(string)
            s[i] = alphabet[n - 1]
            s[i + 1 + n] = alphabet[n - 1]
            solutions += langford(n - 1, s)
    return map("".join, solutions)

n = 3
for l in langford(n, [None] * n * 2): print l
