from random import choice

def num_conflicts(variable, value, state, graph):
	conflicting_neighbors = [neighbor for neighbor in graph[variable] if state[neighbor] == value]
	return len(conflicting_neighbors)

def min_conflicts(problem, max_steps=1000):
	graph, values = problem
	variables = graph.keys()
	
	# for the initial assignment of values to variables,
	# assign values to variables at random
	curr_state = {var: choice(values) for var in variables}

	for _ in range(max_steps):
		# if no variables have any conflicts, then the problem is solved
		conflicted_vars = [var for var in variables if num_conflicts(var, curr_state[var], curr_state, graph)]
		if not conflicted_vars:
			return curr_state

		variable = choice(conflicted_vars)

		# given the conflicted variable that we've chosen at random,
		# take the variable value that produces a minimal number of conflicts
		# if there are multiple such values, pick one at random
		conflicts = [num_conflicts(variable, val, curr_state, graph) for val in values]
		min_indices = [i for i in range(len(values)) if conflicts[i] == min(conflicts)]
		index = choice(min_indices)
		value = values[index]
		
		curr_state[variable] = value
		
	return None

def vertex_coloring(graph, colors):
	return min_conflicts((graph, colors))
	
colors = ['red', 'green', 'blue']

graph = {}
graph['WA'] = {'NT', 'SA'}
graph['NT'] = {'WA', 'SA', 'Q'}
graph['SA'] = {'WA', 'NT', 'Q', 'NSW', 'V'}
graph['V'] = {'SA', 'NSW'}
graph['Q'] = {'NT', 'SA', 'NSW'}
graph['T'] = {}
graph['NSW'] = {'SA', 'Q', 'V'}

solution = vertex_coloring(graph, colors)
print(solution)
