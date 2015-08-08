# an independent set of a graph is a set of vertices s.t.
# no vertex is adjacent to any other vertex in the set
# a maximum independent set contains the largest possible number of such vertices
# max_independent_set(tree, root) finds a maximum independent set of a tree, given the tree and its root

# memoize, because the subproblems overlap
memo = {}

def max_independent_set(tree, root):
	# the big idea:
	# find the maximum independent set of the tree by 
	# finding the m.i.s. of every subtree below the given root
	# and either the maximum independent set includes the root or it doesn't
	# so, you can find the maximum independent set by
	# comparing the m.i.s. of every subtree while including the root and not including the root
	
	# base case: a leaf
	# a root with empty subtrees is the m.i.s.
	# because it is the only non-adjacent vertex
	children = tree[root]
	if not children: 
		return [root]
	
	# don't solve a subproblem that's already been solved
	if root in memo:
		return memo[root]
	
	# the maximum independent set not including the root
	ninc = [m for c in children for m in max_independent_set(tree, c)]
	
	# the maximum independent set including the root
	# note: if you include the root, then you can't include its children
	# because it is adjacent to its children
	# so, recurse on the children's children
	grandchildren = [w for v in children for w in tree[v]]
	inc = [root] + [m for g in grandchildren for m in max_independent_set(tree, g)]
	
	# take the maximum of the two
	memo[root] = max([inc, ninc], key=lambda x: len(x))
	return memo[root]

tree = {0: [1], 1: [2, 3, 4], 3: [], 2: [5, 6], 5: [], 6: [], 4: [7, 8], 7: [], 8: []}
root = 0
print max_independent_set(tree, root)
