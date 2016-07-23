def bsearch_recur(nums, target, lo=0, hi=None):
	if hi == None:
		hi = len(nums) - 1

	if lo > hi:
		return False

	mid = (lo + hi) // 2
	if nums[mid] == target:
		return mid
	elif target > nums[mid]:
		return bsearch_recur(nums, target, mid + 1, hi)
	else:
		return bsearch_recur(nums, target, lo, mid - 1)

def bsearch_iter(nums, target):
	lo = 0
	hi = len(nums) - 1
	
	while lo <= hi:
		mid = (lo + hi) // 2
		if nums[mid] == target:
			return mid
		elif target > nums[mid]:
			lo = mid + 1
		else:
			hi = mid - 1
	
	return False
	
N = 10

nums = list(range(1, N))
print(nums)

target = 6
print(bsearch_recur(nums, target))
print(bsearch_iter(nums, target))
