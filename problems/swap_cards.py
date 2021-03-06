# https://icpcarchive.ecs.baylor.edu/external/75/7514.pdf

def is_goal(state):
	# the state is a goal-state iff 
	# no black card comes before a red card
	# so, check whether you see a black card and then a red card
	
	red = {'h', 'd'}
	black = {'s', 'c'}
	saw_black = False
	
	for card in state:
		suit = card[-1]
		if saw_black and suit in red:
			return False
		elif suit in black:
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
	seen = {init_state}
	queue = [init_state]
	num_swaps = {init_state: 0}

	while queue:
		state = queue.pop(0)
		if is_goal(state):
			return num_swaps[state]
			
		for succ in successors(state):
			if succ not in seen:
				seen.add(succ)
				queue.append(succ)
				num_swaps[succ] = num_swaps[state] + 1

def solve(start): 
	return min_swaps(tuple(start.split()))

start = '2_h A_s K_d'
#start = '2_h A_d K_s K_s'
#start = 'A_d K_s 2_h K_c 10_h J_d'
print(solve(start))
