from min_conflicts import min_conflicts
import nqueens

def queens(N=8):
	variables = list(range(N))	
	values = dict((var, list(range(N))) for var in variables)
	
	constraints = {}
	row_constraint = lambda col1, row1, col2, row2: row1 != row2
	diagonal_constraint = lambda col1, row1, col2, row2: abs(row1 - row2) != abs(col1 - col2)
	for var1 in variables:
		constraints[var1] = []
		for var2 in variables:
			if var1 != var2:
				constraints[var1].append([var2, row_constraint])
				constraints[var1].append([var2, diagonal_constraint])
	
	csp = (variables, values, constraints)
	
	return min_conflicts(csp)

N = 8	
soln = queens(N)
soln = [soln[k] for k in sorted(soln.keys())]
print(soln)

# test the min-conflicts solution
# we know that the backtrack solution is correct
# so, compare the answers
solutions = nqueens.queens(N)
assert soln in solutions
