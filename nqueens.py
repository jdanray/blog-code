# finds all solutions for instances of the N queens problem
# e.g., queens(8) => all 92 solutions of the 8 queens problem
def queens(N=8, sol=[]):
	col = len(sol)	# the current column to be solved
	
	# all the columns have been solved
	if col == N: return [sol]

	# build the list of solutions
	# for each column, iterate over all rows and try the feasible ones
	solutions = []
	for row in range(N):
		# test whether a queen is already on this row
		if row in sol: continue
		
		# test whether a queen is on this diagonal
		sol_cols = range(col)
		if row + col in [sol[c] + c for c in sol_cols]: continue
		if row - col in [sol[c] - c for c in sol_cols]: continue

		# try this row and recurse
		solutions.extend(queens(N, sol + [row]))

	return solutions
