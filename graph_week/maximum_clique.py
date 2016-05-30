# https://www.reddit.com/r/dailyprogrammer/comments/4j65ls/20160513_challenge_266_hard_finding_friends_in/

import build_graph as bg

def maximum_clique(graph, vertices, clique=set()):
	if not vertices:
		return clique

	return max((maximum_clique(graph, vertices & graph[v], clique | {v}) for v in vertices), key=len)

file_location = 'maximum_clique_input.txt'
print(maximum_clique(*bg.build_graph(file_location)))
