def knapsack_recur_naive(values, weights, capacity, i=0):
	if i >= len(weights) or capacity <= 0:
		return 0

	leave_i = knapsack_recur_naive(values, weights, capacity, i + 1)
	if weights[i] > capacity:
		return leave_i
	else:
		pack_i = values[i] + knapsack_recur_naive(values, weights, capacity - weights[i], i + 1)
		return max(pack_i, leave_i)

memo = {}
def knapsack_recur_memo(values, weights, capacity, i=0):
	if i >= len(weights) or capacity <= 0:
		return 0
	
	if not (capacity, i) in memo:
		leave_i = knapsack_recur_memo(values, weights, capacity, i + 1)
		if weights[i] > capacity:
			memo[(capacity, i)] = leave_i
		else:
			pack_i = values[i] + knapsack_recur_memo(values, weights, capacity - weights[i], i + 1)
			memo[(capacity, i)] = max(pack_i, leave_i)
			
	return memo[(capacity, i)]

def knapsack_dp(values, weights, capacity):
	m = len(values)
	V = [[0 for _ in range(capacity + 1)] for _ in range(m + 1)]

	for i in range(1, m + 1):
		for w in range(1, capacity + 1):
			if weights[i - 1] > w:
				V[i][w] = V[i - 1][w]
			else:
				V[i][w] = max(values[i - 1] + V[i - 1][w - weights[i - 1]], V[i - 1][w])

	return V[m][capacity]
	
values = [60, 85, 75, 150]
weights = [20, 50, 30, 70]
capacity = 100
print(knapsack_recur_naive(values, weights, capacity))
print(knapsack_recur_memo(values, weights, capacity))
print(knapsack_dp(values, weights, capacity))
# output: 225
