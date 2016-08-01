# https://icpcarchive.ecs.baylor.edu/external/75/7514.pdf

def solve_one_func(start):
	init_state = tuple(start.split())
	
	seen = [init_state]
	queue = [init_state]
	num_swaps = {init_state: 0}

	while queue:
		state = queue.pop(0)
		
		saw_black = False
		is_goal = True	
		for card in state:
			if saw_black and (card[-1] == 'h' or card[-1] == 'd'):
				is_goal = False
				break
			elif card[-1] == 's' or card[-1] == 'c':
				saw_black = True

		if is_goal:
			return num_swaps[state]
			
		successors = []
		for i in range(len(state) - 1):
			succ = list(state)
			succ[i], succ[i + 1] = succ[i + 1], succ[i]
			successors.append(tuple(succ))
			
		for succ in successors:
			if succ not in seen:
				seen.append(succ)
				queue.append(succ)
				num_swaps[succ] = num_swaps[state] + 1

def is_goal(state):
	# the state is a goal-state iff 
	# no black card comes before a red card
	# so, check whether you see a black card and then a red card
	saw_black = False
	for card in state:
		if saw_black and (card[-1] == 'h' or card[-1] == 'd'):
			return False
		elif card[-1] == 's' or card[-1] == 'c':
			saw_black = True

	return True

def successors(state):
	successors = []
	
	# perform all possible swaps
	# you can only swap adjacent cards
	for i in range(len(state) - 1):
		succ = list(state)
		succ[i], succ[i + 1] = succ[i + 1], succ[i]
		successors.append(tuple(succ))
		
	return successors

# breadth-first search
def min_swaps(init_state):
	seen = [init_state]
	queue = [init_state]
	num_swaps = {init_state: 0}

	while queue:
		state = queue.pop(0)
		if is_goal(state):
			return num_swaps[state]
			
		for succ in successors(state):
			if succ not in seen:
				seen.append(succ)
				queue.append(succ)
				num_swaps[succ] = num_swaps[state] + 1

def solve(start): 
	return min_swaps(tuple(start.split()))

start = '2_h A_s K_d'
#start = '2_h A_d K_s K_s'
#start = 'A_d K_s 2_h K_c 10_h J_d'
print(solve(start))
print(solve_one_func(start))
