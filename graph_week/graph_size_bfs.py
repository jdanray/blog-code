INFINITY = 100000

def build_graph(file_location):
	graph = {}
	vertices = set()
	
	with open(file_location, 'r') as f:
		next(f)
		for edge in f:
			u, v = map(int, edge.split())
			
			vertices.add(u)
			vertices.add(v)
			
			if u in graph:
				graph[u].add(v)
			else:
				graph[u] = {v}
				
	return graph, vertices

def eccentricities(graph, vertices):
	ecc = [eccentricity(graph, u) for u in vertices]
	return [e for e in ecc if e != None]

def eccentricity(graph, u):
	dists = []

	for v in vertices:
		if u is not v:
			d = distance(graph, u, v)
			if d is not None:
				dists.append(d)
			
	if dists:
		return max(dists)
	else:
		return None
	
def distance(graph, s, t):
	dist = {}
	for u in vertices: 
		dist[u] = INFINITY
	dist[s] = 0
	
	q = [s]
	
	while q:
		u = q.pop(0)
		
		if u == t:
			return dist[u]
	
		if not u in graph:
			continue
			
		for v in graph[u]:
			if dist[v] == INFINITY:
				dist[v] = dist[u] + 1
				q.append(v)

	return None
	
file_location = 'graph_size_input.txt'	
graph, vertices = build_graph(file_location)
ecc = eccentricities(graph, vertices)
radius = min(ecc)
diameter = max(ecc)
print('radius: %i\ndiameter: %i' % (radius, diameter))
