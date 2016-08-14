# https://icpcarchive.ecs.baylor.edu/external/35/3580.pdf
# https://jdanray.wordpress.com/2015/03/25/marbles-in-three-baskets/

def goal(node):
	return node[0] == node[1] and node[1] == node[2]

def children(node):
	children = []
	
	for i in range(3):
		for j in range(3):
			if i != j and node[i] >= node[j]:
				child = list(node)
				child[i] -= child[j]
				child[j] += child[j]
				children.append(tuple(child))

	return children

def shortest_path(source):
	seen = {source}
	p = {source: []}
	queue = [source]

	while queue:
		u = queue.pop(0)
		if goal(u):
			return p[u] + [u]
			
		for v in children(u):
			if not v in seen:
				seen.add(v)
				queue.append(v)
				p[v] = p[u] + [u]
				
	return [source]

def solve(s):
	for u in shortest_path(s):
		print(''.join(str(m).rjust(4) for m in u))
	print('============')
	
solve((6,7,11))
solve((15,18,3))
solve((5,6,7))
