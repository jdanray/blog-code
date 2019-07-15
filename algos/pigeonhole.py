import testsort

def pigeonhole(nums):
	m = min(nums)
	N = max(nums) - m + 1
	holes = [0 for _ in range(N)]
	for n in nums: 
		holes[n - m] += 1

	i = 0
	for c in range(N):
		while holes[c] > 0:
			holes[c] -= 1
			nums[i] = c + m
			i += 1

	return nums

testsort.test(pigeonhole)
