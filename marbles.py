import Queue

def goal(node):
    return node[0] == node[1] and node[1] == node[2]

def children(node):
    children = []
    if node[0] >= node[1]:
        children += [[node[0] - node[1], node[1] + node[1], node[2]]]
    if node[0] >= node[2]:
        children += [[node[0] - node[2], node[1], node[2] + node[2]]]
    if node[1] >= node[0]:
        children += [[node[0] + node[0], node[1] - node[0], node[2]]]
    if node[1] >= node[2]:
        children += [[node[0], node[1] - node[2], node[2] + node[2]]]
    if node[2] >= node[0]:
        children += [[node[0] + node[0], node[1], node[2] - node[0]]]
    if node[2] >= node[1]:
        children += [[node[0], node[1] + node[1], node[2] - node[1]]]
    return children

def shortest_path(source):
    q = Queue.Queue()
    q.put(source)
    seen = [source]
    p = {}
    p[str(source)] = None
    while not q.empty():
	u = q.get()
	if goal(u):
		path = []
		while u is not None:
			path.append(u)
			u = p[str(u)]
		return path
	for v in children(u):
		if not v in seen:
			seen.append(v)
			q.put(v)
			p[str(v)] = u
    return None

def solve(s):
    path = shortest_path(s)
    if not path:
        path = [s]
    while path:
        v = path.pop()
        print str(v[0]).rjust(4) + str(v[1]).rjust(4) + str(v[2]).rjust(4)
    print "============"

solve([6,7,11])
solve([15,18,3])
solve([5,6,7])
