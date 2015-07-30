# given preferences for each man and preferences for each woman,
# find a stable matching between the men and women
def gale_shapley(mprefs, wprefs):
	# test whether there are as many men as women
	assert(len(mprefs) == len(wprefs))
	N = len(mprefs)

	# gale_shapley(mprefs, wprefs) => matching
	# mprefs[m] is the list of man m's preferences
	# e.g., if mprefs[0] = [0, 1, 2], then
	# man 0's preferences are: woman 0 > woman 1 > woman 2
	# wprefs[w] is the list of woman w's preferences	
	# matching[w] is the man that woman w has accepted
	matching = [None] * N
	
	# if wchoice[w][m] = i, then
	# man m is woman w's i-th choice
	# (previously i just used wprefs[w].index(m)
	# but index() is O(n) in python
	# with this smarter data structure, the algo is faster)
	wchoice = [[None] * N for _ in range(N)]
	for w, woman in enumerate(wprefs):
		for m, man in enumerate(woman):
			wchoice[w][man] = m
	
	# if next_woman[m] = w, then 
	# man m proposes to the w-th woman on his list next
	# initially each man proposes to the zeroth (first) woman on his list
	next_woman = [0] * N
	
	# initially every man is unengaged
	# until every man is engaged, each unengaged man proposes to the next woman on his list
	# if the woman is unmatched, match her with the unengaged man
	# if she is matched but prefers the unengaged man to her fiance,
	# match her with the unengaged man and make her fiance unengaged
	# if neither, the man remains unengaged and moves onto the next woman
	unengaged_men = range(N)
	while unengaged_men:
		man = unengaged_men.pop(0)
		woman = mprefs[man][next_woman[man]]
		next_woman[man] += 1
		if matching[woman]:
			if wchoice[woman][man] < wchoice[woman][matching[woman]]:
				unengaged_men.append(matching[woman])
				matching[woman] = man
			else: unengaged_men.append(man)
		else: matching[woman] = man

	return matching
	
print gale_shapley([[0, 1, 2], [2, 1, 0], [1, 0, 2]], [[1, 2, 0], [2, 1, 0], [0, 1, 2]])
