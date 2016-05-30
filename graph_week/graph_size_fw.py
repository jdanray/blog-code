# https://www.reddit.com/r/dailyprogrammer/comments/4iut1x/20160511_challenge_266_intermediate_graph_radius/

import build_graph as bg

def eccentricities(graph, vertices):
	ecc = []
	dist = floyd_warshall(graph, vertices)
	
	for u in dist:
		d = [dist[u][v] for v in dist[u] if dist[u][v] != INFINITY]
		if d: ecc.append(max(d))
		
	return ecc
	
def floyd_warshall(graph, vertices):
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
ecc = eccentricities(*bg.build_graph(file_location, True))
radius = min(ecc)
diameter = max(ecc)
print('radius: %i\ndiameter: %i' % (radius, diameter))
