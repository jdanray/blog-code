from random import choice

def num_conflicts(variable, value, state, constraints):
	# constraints is a dictionary of the form
	# {variable1: [[var_1, relation_1], [var_2, relation_2], ..., [var_n, relation_n]], variable2: ...}
	# where relation_i is a relation that the given value and the value of var_i must satisfy
	
	return sum(1 if not relation(variable, value, var, state[var]) else 0 for var, relation in constraints[variable])

def min_conflicts(csp, max_steps=1000):
	variables, values, constraints = csp
	
	# for the initial assignment of values to variables,
	# assign values to variables at random
	curr_state = dict((var, choice(values[var])) for var in variables)

	for _ in range(max_steps):
		# if no variables have any conflicts, then the problem is solved
		conflicting_vars = [var for var in variables if num_conflicts(var, curr_state[var], curr_state, constraints)]
		if not conflicting_vars:
			return curr_state

		variable = choice(conflicting_vars)

		# given the conflicting variable that we've chosen at random,
		# take the variable value that produces a minimal number of conflicts
		# if there are multiple such values, pick one at random
		conflicts = [num_conflicts(variable, val, curr_state, constraints) for val in values[variable]]
		min_conf = min(conflicts)
		min_indices = [i for i, c in enumerate(conflicts) if c == min_conf]
		index = choice(min_indices)
		value = values[variable][index]
		
		curr_state[variable] = value
		
	return None
