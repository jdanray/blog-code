# given a directed acylic graph,
# find a linear ordering such that u precedes v
# for every directed edge uv
def toposort(dag):
	explored = set()
	sorting = []

	def dfs(u):
		explored.add(u)
		for v in dag.get(u, []):
        		if v not in explored:
				dfs(v)
		sorting.insert(0, u)		

	for u in dag:
		if u not in explored:
      			dfs(u)
	
	return sorting
