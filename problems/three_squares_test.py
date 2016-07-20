# see https://jdanray.wordpress.com/2016/04/05/magic-squares/

# computed via
# three_squares = [sq for sq in itertools.permutations(range(1, 3 ** 2 + 1)) if is_magic_square(sq)]
three_squares = [(2, 7, 6, 9, 5, 1, 4, 3, 8), (2, 9, 4, 7, 5, 3, 6, 1, 8), (4, 3, 8, 9, 5, 1, 2, 7, 6), (4, 9, 2, 3, 5, 7, 8, 1, 6), (6, 1, 8, 7, 5, 3, 2, 9, 4), (6, 7, 2, 1, 5, 9, 8, 3, 4), (8, 1, 6, 3, 5, 7, 4, 9, 2), (8, 3, 4, 1, 5, 9, 6, 7, 2)]

# numericize([1, 2, 3]) == 123
def numericize(entry): return sum(e * 10 ** (len(entry) - i - 1) for i, e in enumerate(entry))

# sqsum([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) == 276^2 + 951^2 + 438^2
def sqsum(entries): return sum(numericize(entry) ** 2 for entry in entries)

def test_three_square(square):
	dim = 3

	rows = [square[i:i + dim] for i in range(0, len(square), dim)]
	columns = [[square[i + j * dim] for j in range(dim)] for i in range(dim)]
	right_diagonal = [[square[i * (dim + 1)] for i in range(dim)]]	
	left_diagonal = [[square[i * (dim - 1)] for i in range(1, dim + 1)]]
	
	square_entries = [rows] + [columns] + [right_diagonal] + [left_diagonal]
	
	return all(sqsum(entry) == sqsum(reversed(entry)) for entry in square_entries)

def test_all_three_squares(): return all(test_three_square(sq) for sq in three_squares)

print(test_all_three_squares())
