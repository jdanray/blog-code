def fib_r(n):
	if n == 1 or n == 0:
		return 1
	else:
		return fib_r(n - 1) + fib_r(n - 2)

memo = {0: 1, 1: 1}
def fib_r_memo(n):
	if n in memo:
		return memo[n]
	else:
		memo[n] = fib_r_memo(n - 1) + fib_r_memo(n - 2)
		return memo[n]

def fib_dp(n):
	memo = {}
	memo[0] = 1
	memo[1] = 1
	for i in range(2, n + 1):
		memo[i] = memo[i - 1] + memo[i - 2]
	return memo[n]

n = 20
print(fib_r(n))
print(fib_r_memo(n))
print(fib_dp(n))
# output: 10946
