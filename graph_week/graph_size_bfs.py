# https://www.reddit.com/r/dailyprogrammer/comments/4iut1x/20160511_challenge_266_intermediate_graph_radius/

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
	ecc = [eccentricity(graph, vertices, u) for u in vertices]
	return [e for e in ecc if e != None]

def eccentricity(graph, vertices, u):
	dist = [d for d in distances(graph, vertices, u).values() if d != INFINITY]
	if dist: return max(dist)
	else:    return None
	
def distances(graph, vertices, s):
	dist = {}
	for u in vertices: 
		dist[u] = INFINITY
	dist[s] = 0
	
	q = [s]
	while q:
		u = q.pop(0)
	
		if not u in graph:
			continue
			
		for v in graph[u]:
			if dist[v] > dist[u] + 1:
				dist[v] = dist[u] + 1
				q.append(v)

	return dist
	
file_location = 'graph_size_input.txt'	
graph, vertices = build_graph(file_location)
ecc = eccentricities(graph, vertices)
radius = min(ecc)
diameter = max(ecc)
print('radius: %i\ndiameter: %i' % (radius, diameter))
