# https://www.reddit.com/r/dailyprogrammer/comments/4iut1x/20160511_challenge_266_intermediate_graph_radius/

def build_graph(file_location):
	graph = {}
	
	with open(file_location, 'r') as f:
		next(f)
		for edge in f:
			u, v = map(int, edge.split())
			if u in graph:
				graph[u].add(v)
			else:
				graph[u] = {v}
				
	return graph

def eccentricities(graph):
	ecc = []
	dist = floyd_warshall(graph)
	
	for u in dist:
		d = [dist[u][v] for v in dist[u] if dist[u][v] != INFINITY]
		if d: ecc.append(max(d))
		
	return ecc
	
def floyd_warshall(graph):
	vertices = set()
	for u in graph:
		vertices.add(u)
		for v in graph[u]:
			vertices.add(v)

	dist = {}
	for u in vertices:
		dist[u] = {}
		for v in vertices:
			dist[u][v] = INFINITY
			
	for u in graph:
		dist[u][u] = 0
		for v in graph[u]:
			dist[u][v] = 1
	
	for k in vertices:
		for i in vertices:
			for j in vertices:
				if dist[i][j] > dist[i][k] + dist[k][j]:
					dist[i][j] = dist[i][k] + dist[k][j]
	
	return dist

INFINITY = 100000
file_location = 'graph_size_input.txt'
graph = build_graph(file_location)
ecc = eccentricities(graph)
radius = min(ecc)
diameter = max(ecc)
print('radius: %i\ndiameter: %i' % (radius, diameter))
