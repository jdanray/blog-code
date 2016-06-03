from dijkstra import dijkstra

def build_graph(file_location):
        graph = {}
	
        with open(file_location, 'r') as f:
                for edge in f:
                        u, v, w = edge.split()
                        w = int(w)
                        
                        if u in graph:
                                graph[u] += [[v, w]]
                        else:
                                graph[u] = [[v, w]]

                        if v in graph:
                                graph[v] += [[u, w]]
                        else:
                                graph[v] = [[u, w]]

        return graph

def main():
	file_location = 'highways.txt'
	graph = build_graph(file_location)
	start = 'Atlanta'
	
	dists, paths = dijkstra(graph, start)
	
	destinations = ['New_York', 'Dallas', 'Chicago']
	for dest in destinations:
		print(dest, dists[dest], ' -> '.join(paths[dest]))

if __name__ == "__main__":
    main()
