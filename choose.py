def choose_r(n, k):
	if k == 0 or k == n:
		return 1
	else:
		return choose_r(n - 1, k - 1) + choose_r(n - 1, k)

memo = {}
def choose_recur_memo(n, k):
	if k == 0 or k == n:
		return 1
	elif not (n, k) in memo:
		memo[(n, k)] = choose_r(n - 1, k - 1) + choose_r(n - 1, k)
	return memo[(n, k)]

def choose_dp(n, k):
	memo = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

	for i in range(n + 1):
		for j in range(min(i, k) + 1):
			if j == 0 or j == i:
				memo[i][j] = 1
			else:
				memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]
				
	return memo[n][k]

n = 10
k = 2
print(choose_r(n, k))
print(choose_recur_memo(n, k))
print(choose_dp(n, k))
# output: 45
