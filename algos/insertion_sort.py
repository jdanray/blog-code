# given a list of numbers, 
# perform an insertion sort on the list
def insertion_sort(nums):
	for i in range(1, len(nums)):
		key = nums[i]
		j = i - 1
		while j >= 0 and nums[j] > key:
			nums[j + 1] = nums[j]
			j -= 1
		nums[j + 1] = key
		
	return nums
