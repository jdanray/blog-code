import testsort

# nums is a list of nonnegative integers
def countsort(nums):
	N = len(nums)
	m = max(nums)

	count = [0 for _ in range(m + 1)]
	for n in nums: 
		count[n] += 1
	for i in range(1, m + 1): 
		count[i] += count[i - 1]

	res = [0 for _ in range(N)]
	for i in range(N - 1, -1, -1):
		res[count[nums[i]] - 1] = nums[i]
		count[nums[i]] -= 1
 
	return res

testsort.test(countsort)
