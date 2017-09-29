def dist(X, Y, ops, cost):
	D = [[0 for _ in range(len(Y) + 1)] for _ in range(len(X) + 1)]
	for i in range(len(X) + 1):
		for j in range(len(Y) + 1):
			if i == 0:
				D[i][j] = j
			elif j == 0:
				D[i][j] = i		
			elif X[i - 1] == Y[j - 1]:
				D[i][j] = D[i - 1][j - 1]
			else:
				D[i][j] = min(D[i + u][j + v] + cost(u, v) for (u, v) in ops)
	return D[len(X)][len(Y)]

deletion = (-1, 0)
insertion = (0, -1)
substitution = (-1, -1)

edit_ops = [deletion, insertion, substitution]
lcs_ops = [deletion, insertion]
hamming_ops = [substitution]

cost = lambda u, v: 1

edit = dist('kitten', 'sitting', edit_ops, cost)
lcs = dist('kitten', 'sitting', lcs_ops, cost)
hamming = dist('kitteng', 'sitting', hamming_ops, cost)

print(edit)
print(lcs)
print(hamming)
