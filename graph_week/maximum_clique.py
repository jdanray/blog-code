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
	if not vertices:
		return clique

	return max((maximum_clique(graph, vertices & graph[v], clique | {v}) for v in vertices), key=len)

file_location = 'maximum_clique_input.txt'
print(maximum_clique(*build_graph(file_location)))
