import testsort

def bubble(nums):
	n = len(nums)
	while n > 1:
		newn = 0
		for i in range(1, n):
			if nums[i] < nums[i - 1]:
				nums[i],  nums[i - 1] = nums[i - 1], nums[i]
				newn = i
		n = newn
	return nums

testsort.test(bubble)
