import Queue

def galeshapley(mprefs, wprefs):
	matches = [None] * len(wprefs)
	unengaged_men = Queue.Queue()
	for m in range(len(mprefs)): unengaged_men.put(m)
	curr_proposee = [0] * len(mprefs)
	
	while not unengaged_men.empty():
		man = unengaged_men.get()
		woman = mprefs[man][curr_proposee[man]]
		curr_proposee[man] -= 1
		if matches[woman]:
			if wprefs.index(man) < wprefs.index(matches[woman]):				
				unengaged_men.put(matches[woman])
				matches[woman] = man
			else: unengaged_men.put(man)
		else: matches[woman] = man

	return matches
	
print galeshapley([[0, 1, 2], [2, 1, 0], [1, 0, 2]], [[1, 2, 0], [2, 1, 0], [0, 1, 2]])
