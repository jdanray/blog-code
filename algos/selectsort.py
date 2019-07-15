import testsort

def selectsort(nums):
	for i in range(len(nums)):
		m = i
		for j in range(i + 1, len(nums)):
			if nums[j] < nums[m]:
				m = j
		nums[i], nums[m] = nums[m], nums[i]
	return nums

testsort.test(selectsort)
