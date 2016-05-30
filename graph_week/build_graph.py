def build_graph(file_location, directed=False):
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
	
			if not directed:
				if v in graph:
					graph[v].add(u)
				else:
					graph[v] = {u}
			
	return graph, vertices
