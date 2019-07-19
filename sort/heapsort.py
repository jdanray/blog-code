import heapq
import testsort

def heapsort(nums):
	heapq.heapify(nums)
	for i in range(len(nums) - 1, 0, -1):
		nums[0], nums[i] = nums[i], nums[0]
		nums.sort()
	return nums

testsort.test(heapsort)
