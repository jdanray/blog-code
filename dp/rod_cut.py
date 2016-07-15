# see CLRS 15.1
# given a rod of length n and a table of prices p_i for i = 0, 1, 2, ..., n,
# finds the maximum revenue obtainable by cutting up the rod and selling the pieces

infinity = 1000000
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def cut(n):
	r, s = list(range(n + 1)), list(range(n + 1))
	for i in range(1, n + 1):
		r[i] = -infinity
		for j in range(1, i + 1):
			q = p[j] + r[i - j]
			if r[i] < q:
				r[i] = q
				s[i] = j
	return r, s

# output solution
for n in range(1, 11):
	r, s = cut(n)
	output = str(r[n]) + " with soln " + str(n) + " = "
	while n > 0:
		output += str(s[n]) + " + "
		n -= s[n]
	print(output[:-3])
