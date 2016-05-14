# https://www.reddit.com/r/dailyprogrammer/comments/4j65ls/20160513_challenge_266_hard_finding_friends_in/

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
	
			if v in graph:
				graph[v].add(u)
			else:
				graph[v] = {u}
			
	return graph, vertices

def maximum_clique(graph, vertices, clique=set()):
	global max_clique

	if not vertices and len(clique) > len(max_clique):
		max_clique = clique

	for v in vertices:
		maximum_clique(graph, vertices & graph[v], clique | {v})

file_location = 'maximum_clique_input.txt'
graph, vertices = build_graph(file_location)
max_clique = set()
maximum_clique(graph, vertices)
print(max_clique)
