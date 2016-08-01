# https://icpcarchive.ecs.baylor.edu/external/75/7513.pdf

def max_area_poster(billboards):
	# brute-force search
	# try every possible poster
	# if it fits a billboard, then count that billboard
	# return the poster that covers the max total area
	
	max_width = max(b[0] for b in billboards)
	max_height = max(b[1] for b in billboards)	
	
	posters = {}
	for w in range(1, max_width + 1):
		for h in range(1, max_height + 1):
			posters[(w, h)] = 0
			for b in billboards:
				if w <= b[0] and h <= b[1]:
					posters[(w, h)] += 1
	
	return max(posters, key=lambda p: p[0] * p[1] * posters[p])
	
billboards = [(1, 4), (2, 2), (4, 1)]
#billboards = [(1, 4), (2, 2), (3, 3), (4, 4)]
print(max_area_poster(billboards))
