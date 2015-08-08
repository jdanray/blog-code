def bfs(graph, s):
    q = [s]
    order = []
    while q:
        u = q.pop(0)
        order.insert(0, u)
        for v in tree[u]:
            q.append(v)
    return order

def mis(tree, root):
	memo = {}
	for node in bfs(tree, root):
		children = tree[node]
		ninc = [m for c in children for m in memo[c]]
		grandchildren = [w for v in children for w in tree[v]]
		inc = [root] + [m for g in grandchildren for m in memo[g]]
		memo[node] = max([inc, ninc], key=lambda x: len(x))
	return memo[root]

tree = {0: [1], 1: [2, 3, 4], 3: [], 2: [5, 6], 5: [], 6: [], 4: [7, 8], 7: [], 8: []}
root = 0
print mis(tree, root)
