# https://www.reddit.com/r/dailyprogrammer/comments/4ijtrt/20160509_challenge_266_easy_basic_graph/

graph = """3 
1 2
1 3"""

graph = graph.splitlines()

num_nodes = int(graph[0])
adj_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

for edge in graph[1:]:
	u, v = map(int, edge.split())
	adj_matrix[u - 1][v - 1] = 1
	adj_matrix[v - 1][u - 1] = 1

for n, row in enumerate(adj_matrix):
	print('Node %i has a degree of %i\n' % (n + 1, sum(row)))

for row in adj_matrix:
	print(' '.join(map(str, row)))
