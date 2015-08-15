# see https://github.com/jdanray/blog-code/blob/master/top_down_mis.py
# for details on the problem and the dynamic program that solves it

# breadth-first traversal
# stores the nodes in reverse order
def bft(tree, start):
    q = [start]
    order = []
    while q:
        u = q.pop(0)
        order = [u] + order
        for v in tree[u]:
            q.append(v)
    return order

# given a tree and its root,
# finds the maximum independent set of the tree
def mis(tree, root):
	memo = {}
	for node in bft(tree, root):
		children = tree[node]
		ninc = [m for c in children for m in memo[c]]
		grandchildren = [w for v in children for w in tree[v]]
		inc = [node] + [m for g in grandchildren for m in memo[g]]
		memo[node] = max([inc, ninc], key=lambda x: len(x))
	return memo[root]

tree = {0: [1], 1: [2, 3, 4], 3: [], 2: [5, 6], 5: [], 6: [], 4: [7, 8], 7: [], 8: []}
root = 0
print mis(tree, root)
