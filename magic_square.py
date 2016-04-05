# see https://www.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/

from math import sqrt
from itertools import permutations

def is_magic_square(grid):
	dim = int(sqrt(len(grid)))
	magic_number = int(dim * (dim ** 2 + 1) / 2)

	rows = [grid[i:i + dim] for i in range(0, len(grid), dim)]
	columns = [[grid[i + j * dim] for j in range(dim)] for i in range(dim)]
	right_diagonal = [[grid[i * (dim + 1)] for i in range(dim)]]	
	left_diagonal = [[grid[i * (dim - 1)] for i in range(1, dim + 1)]]
	
	grid_entries = rows + columns + right_diagonal + left_diagonal

	return all(sum(e for e in entry) == magic_number for entry in grid_entries)

grid = [8, 1, 6, 3, 5, 7, 4, 9, 2]
grid = [2, 7, 6, 9, 5, 1, 4, 3, 8]
grid = [3, 5, 7, 8, 1, 6, 4, 9, 2]
grid = [8, 1, 6, 7, 5, 3, 4, 9, 2]
print(is_magic_square(grid))

def is_partial_magic_square(partial_grid):
	# find the length of the entire grid
	n = 0
	while len(partial_grid) + n != n ** 2: n += 1
	grid_length = n ** 2
	
	#missing_entries = [e for e in range(1, grid_length + 1) if e not in partial_grid]
	missing_entries = set(range(1, grid_length + 1)) - set(partial_grid)
	
	return any(is_magic_square(partial_grid + list(bottom_row)) for bottom_row in permutations(missing_entries))

partial_grid = [8, 1, 6, 3, 5, 7]
partial_grid = [3, 5, 7, 8, 1, 6]
print(is_partial_magic_square(partial_grid))
