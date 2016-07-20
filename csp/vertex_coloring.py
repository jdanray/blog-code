from min_conflicts import min_conflicts

def vertex_coloring(graph, colors):
	variables = graph.keys()
	
	values = dict((var, colors) for var in variables)
	
	cons = lambda var1, value1, var2, value2: value1 != value2
	constraints = {}
	for u in graph:
		constraints[u] = []
		for v in graph[u]:
			constraints[u].append([v, cons])

	csp = (variables, values, constraints)

	return min_conflicts(csp)
	
graph = {}
graph['WA'] = ['NT', 'SA']
graph['NT'] = ['WA', 'SA', 'Q']
graph['SA'] = ['WA', 'NT', 'Q', 'NSW', 'V']
graph['V'] = ['SA', 'NSW']
graph['Q'] = ['NT', 'SA', 'NSW']
graph['T'] = []
graph['NSW'] = ['SA', 'Q', 'V']

colors = ['red', 'green', 'blue']

solution = vertex_coloring(graph, colors)
print(solution)

# test the solution
for u in graph:
	for v in graph[u]:
		assert solution[u] != solution[v]
