import Queue

# given preferences for each man and preferences for each woman,
# find a stable matching between the men and women
def gale_shapley(mprefs, wprefs):
	# gale_shapley(mprefs, wprefs) => matches
	# mprefs[m] is the list of man m's preferences
	# wprefs[w] is the list of woman w's preferences	
	# matches[w] is the man that woman w has accepted
	matches = [None] * len(wprefs)
	
	# if next_proposee[m] = w, then 
	# man m proposes to the wth woman on his list next
	# initially each man proposes to the zeroth (first) woman on his list
	next_proposee = [0] * len(mprefs)
	
	# initially every man is unengaged
	unengaged_men = Queue.Queue()
	for m in range(len(mprefs)): unengaged_men.put(m)
	
	# until every man is engaged, go down each unengaged man's list of preferences
	# if a woman is unmatched, match her with the unengaged man
	# if she is matched but she prefers the unengaged man to her fiance,
	# match her with the unengaged man and make her fiancee unengaged
	while not unengaged_men.empty():
		man = unengaged_men.get()
		woman = mprefs[man][next_proposee[man]]
		next_proposee[man] -= 1
		if matches[woman]:
			if wprefs.index(man) < wprefs.index(matches[woman]):				
				unengaged_men.put(matches[woman])
				matches[woman] = man
			else: unengaged_men.put(man)
		else: matches[woman] = man

	return matches
	
print gale_shapley([[0, 1, 2], [2, 1, 0], [1, 0, 2]], [[1, 2, 0], [2, 1, 0], [0, 1, 2]])
