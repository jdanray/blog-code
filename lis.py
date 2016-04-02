# given a sequence of integers,
# finds the longest increasing subsequence
def lis(seq):
	memo = []
	for i, s in enumerate(seq):
		longest = []
		for j in range(i):
			if seq[j] <= s and len(memo[j]) > len(longest):
				longest = memo[j]
		memo.append(longest + [s])
	return max(memo, key=len)

s = [10,20,1,30,40,2,50,3,4,5,6,7,8,9]
print lis(s)    
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
