# count the number of ways to make change for a given amount
# it's equal to the number of ways without using the first denomination,
# plus the number of ways using the first denomination

def count_change_recur(amount, denoms, i=0):
	if amount == 0:
		return 1
	elif amount < 0 or i >= len(denoms):
		return 0
	else:
		return count_change_recur(amount, denoms, i + 1) + count_change_recur(amount - denoms[i], denoms, i)

memo = {}
def count_change_memo(amount, denoms, i=0):
	if amount == 0:
		return 1
	elif amount < 0 or i >= len(denoms):
		return 0
	elif (amount, i) not in memo:
		memo[(amount, i)] = count_change_memo(amount, denoms, i + 1) + count_change_memo(amount - denoms[i], denoms, i)
	return memo[(amount, i)]

def count_change_dp(amount, denoms):
	count = [[0 for _ in range(len(denoms) + 1)] for _ in range(amount + 1)]
	for j in range(len(denoms) + 1):
		count[0][j] = 1
	for i in range(1, amount + 1):
		for j in range(1, len(denoms) + 1):
			# count[i][j - 1] == no. ways w/o using denomination
			if denoms[j - 1] > i:
				count[i][j] = count[i][j - 1]
			else:
				count[i][j] = count[i][j - 1] + count[i - denoms[j - 1]][j]
	return count[amount][len(denoms)]

print(count_change_recur(100, [50, 25, 10, 5, 1])) # 292
print(count_change_memo(100, [50, 25, 10, 5, 1]))  # 292
print(count_change_dp(100, [50, 25, 10, 5, 1]))    # 292
print(memo)
