# given two sequences of integers,
# finds the length of the longest common subsequence

def lcs_recur_naive(x, y, i=0, j=0):
	if i >= len(x):
		return 0
	elif j >= len(y):
		return 0
	elif x[i] == y[j]:
		return 1 + lcs_recur_naive(x, y, i + 1, j + 1)
	else:
		return max(lcs_recur_naive(x, y, i + 1, j), lcs_recur_naive(x, y, i, j + 1))

memo = {}
def lcs_recur_memo(x, y, i=0, j=0):
	if i >= len(x):
		return 0
	elif j >= len(y):
		return 0
	elif not (i, j) in memo:
		if x[i] == y[j]:
			memo[(i, j)] = 1 + lcs_recur_memo(x, y, i + 1, j + 1)
		else:
			memo[(i, j)] = max(lcs_recur_memo(x, y, i + 1, j), lcs_recur_memo(x, y, i, j + 1))
			
	return memo[(i, j)]
		
def lcs_dp(x, y):
	m = len(x)
	n = len(y)
	L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
	
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if x[i - 1] == y[j - 1]:
				L[i][j] = L[i - 1][j - 1] + 1
			else:
				L[i][j] = max(L[i - 1][j], L[i][j - 1])   
				
	return L[m][n]
	
x = [2,4,6,8,10]
y = [1,2,3,4,5,6,7,8,9,10]
print(lcs_recur_naive(x, y))
print(lcs_recur_memo(x, y))
print(lcs_dp(x, y))
# output: 5
