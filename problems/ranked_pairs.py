# determines whether a given graph has a cycle in it
# c/o http://www.geeksforgeeks.org/detect-cycle-in-a-graph/
def is_cyclic(graph):
	def _is_cyclic(graph, u, visited, stack):
		if u not in visited:
			if u not in graph:
				return False
			
			visited.add(u)		
			stack[u] = True
			
			for v in graph[u]:
				if v not in visited and _is_cyclic(graph, v, visited, stack):
					return True
				elif v in stack:
					return True

		stack.pop(u)
		return False

	return any(_is_cyclic(graph, u, set(), {}) for u in graph)

# given a set of preferences and a set of candidates,
# for each pair of candidates (x, y),
# count all the times that x was ranked ahead of y
def tally(preferences, candidates):				
	votes = {x: {y: 0 for y in candidates} for x in candidates}

	for pref in preferences:
		for i in range(len(pref)):
			for j in range(i + 1, len(pref)):
				votes[pref[i]][pref[j]] += 1
				
	return votes

# x is a majority over y if x has more votes than y
# find all majorities
def majorities(votes, candidates):
	return {(x, y) for x in candidates for y in candidates if votes[x][y] > votes[y][x]}

# ensure that the majorities don't produce a cycle
# {(a, b), (b, c), (c, a)} is cyclic, because a->b->c->a
# treat the sorted list of majorities like a directed acyclic graph
# if x is a majority over y, then there is a directed edge from x to y
# try to add edges to the dag
# if an edge would produce a cycle, don't add it
def lock_in(majorities):
	graph = {}
	
	for m in majorities:
		u, v = m
		
		new_graph = dict(graph)
		if u not in new_graph:
			new_graph[u] = {v}
		else:
			new_graph[u].add(v)
			
		if not is_cyclic(new_graph):
			graph = new_graph
			
	return graph

# given a set of individual preferences and a set of candidates,
# aggregate the individual preferences into one overall group preferences
def ranked_pairs(preferences, candidates):
	# tally
	votes = tally(preferences, candidates)
	majs = majorities(votes, candidates)
	
	# sort
	majs = sorted(majs, key=lambda m: votes[m[0]][m[1]], reverse=True)
	
	# lock in
	dag = lock_in(majs)

	# order candidates by how many outgoing edges they have in the dag
	return tuple(sorted(dag, key=lambda u: len(dag[u]), reverse=True))

candidates = {1, 2, 3, 4, 5}
preferences = {(3, 4, 1, 2, 5), (4, 3, 1, 2, 5), (4, 1, 2, 3, 5), (4, 1, 2, 3, 5), \
(4, 1, 2, 3, 5), (1, 4, 2, 3, 5), (1, 3, 5, 2, 4), (4, 1, 3, 2, 5), (4, 2, 1, 3, 5), \
(4, 2, 5, 3, 1), (4, 2, 3, 5, 1), (4, 1, 3, 2, 5), (4, 1, 3, 2, 5), (2, 4, 3, 1, 5), \
(2, 1, 3, 5, 4), (4, 3, 1, 5, 2), (3, 4, 1, 2, 5)}
ranking = ranked_pairs(preferences, candidates)
print(ranking)
