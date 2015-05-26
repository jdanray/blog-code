# given a directed acylic graph,
# find a linear ordering such that u precedes v
# for every directed edge uv
def topo_sort(dag):
  explored = []
  sorting = []

  def dfs(u):
    explored.append(u)
    if u in dag:
      for v in dag[u]:
        if not v in explored:
				  dfs(v)
		sorting.insert(0, u)		

  for u in dag:
    if not u in explored:
      dfs(u)
	
	return sorting
