# https://www.reddit.com/r/dailyprogrammer/comments/4iut1x/20160511_challenge_266_intermediate_graph_radius/

import build_graph as bg

INFINITY = 100000

def eccentricities(graph, vertices):
	ecc = [eccentricity(graph, vertices, u) for u in vertices]
	return [e for e in ecc if e != None]

def eccentricity(graph, vertices, u):
	dist = bfs(graph, vertices, u)
	dist = [dist[v] for v in dist.keys() if v != u and dist[v] != INFINITY]
	if dist: return max(dist)
	else:    return None
	
def bfs(graph, vertices, s):
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
ecc = eccentricities(*bg.build_graph(file_location, True))
radius = min(ecc)
diameter = max(ecc)
print('radius: %i\ndiameter: %i' % (radius, diameter))
