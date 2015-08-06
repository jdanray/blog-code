# https://icpcarchive.ecs.baylor.edu/external/64/6476.pdf

# BFS/DIJKSTRA SOLUTION

# DFS finds every possible solution and then returns the optimal one
# BFS/Dijkstra is guaranteed to find the optimal solution first, so once you find one solution, you can quit

import heapq

def bfs_navigate(start):
	q = []
	heapq.heappush(q, [start, 0])
	traveled = [start]
	zombies = {}		# no. of zombies met by the time you get to a specific outpost
	zombies[start] = 0	# initially you've met no zombies
	ammo = 0

	while q:
		# grab your current outpost location and
		# the number of zombies you encountered
		loc, shot = heapq.heappop(q)

		# you've reached the outpost that has supplies
		if supplies[loc]:
			return zombies[loc]
		
		# subtract amount of ammo used to shoot zombies
		ammo -= shot
		
		# take ammo from outpost you're at
		ammo += reloads[loc]
		reloads[loc] = 0

		# push adjacent outposts onto the queue		
		for v in graph[loc]:
			outpost, threats = v
			if outpost not in traveled and threats <= ammo:
				zombies[outpost] = zombies[loc] + threats
				heapq.heappush(q, [outpost, threats])
				traveled.append(outpost)

	# you couldn't reach the supplies outpost				
	return "No safe path"

reloads = {'origin': 5, 'nulo': 0, 'target': 0}
supplies = {'origin': False, 'nulo': False, 'target': True}
graph = {'origin': [['nulo', 1], ['target', 20]], 'nulo': [['target', 1], ['origin', 1]], 'target': [['origin', 20], ['nulo', 1]]}

print bfs_navigate('origin')

reloads = {'origin': 1, 'nulo': 0, 'target': 0}
supplies = {'origin': False, 'nulo': False, 'target': True}
graph = {'origin': [['nulo', 1]], 'nulo': [['target', 1], ['origin', 1]], 'target': [['nulo', 1]]}

print bfs_navigate('origin')

reloads = {'origin': 1, 'ammuni': 1, 'target': 0}
supplies = {'origin': False, 'ammuni': False, 'target': True}
graph = {'origin': [['ammuni', 1]], 'ammuni': [['target', 1], ['origin', 1]], 'target': [['ammuni', 1]]}
	
print bfs_navigate('origin')

# DFS RECURSIVE BACKTRACKING SOLUTION

def dfs_navigate(start, shot=0, ammo=0):
	# you reached the outpost that has supplies
	if supplies[start]:
		return [shot]

	# take ammo from outpost you're at
	ammo += reloads[start]
	reloads[start] = 0

	# recurse on every possible adjacent outpost
	# keep track of how many zombies you encountered and
	# how much ammo you used
	zombies = []
	for node in graph[start]:
		outpost, threats = node
		if threats <= ammo:
			zombies += dfs_navigate(outpost, shot + threats, ammo - threats)
	return zombies

def solve(start):
	# find the number of zombies on each possible path
	# take the minimum number of zombies
	zombies = dfs_navigate(start)
	if zombies:
		print min(zombies)
	else:
		print "No safe path"

reloads = {'origin': 5, 'nulo': 0, 'target': 0}
supplies = {'origin': False, 'nulo': False, 'target': True}
graph = {'origin': [['nulo', 1], ['target', 20]], 'nulo': [['target', 1], ['origin', 1]], 'target': [['origin', 20], ['nulo', 1]]}

solve('origin')

reloads = {'origin': 1, 'nulo': 0, 'target': 0}
supplies = {'origin': False, 'nulo': False, 'target': True}
graph = {'origin': [['nulo', 1]], 'nulo': [['target', 1], ['origin', 1]], 'target': [['nulo', 1]]}

solve('origin')

reloads = {'origin': 1, 'ammuni': 1, 'target': 0}
supplies = {'origin': False, 'ammuni': False, 'target': True}
graph = {'origin': [['ammuni', 1]], 'ammuni': [['target', 1], ['origin', 1]], 'target': [['ammuni', 1]]}

solve('origin')
