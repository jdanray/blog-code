import testsort

def quicksort(lst):
	if not lst:
		return []

	pivot = lst[0]
	lt = [elem for elem in lst if elem < pivot]
	eq = [elem for elem in lst if elem == pivot]
	gt = [elem for elem in lst if elem > pivot]
	return quicksort(lt) + eq + quicksort(gt)

testsort.test(quicksort)
