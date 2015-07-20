# given preferences for each man and preferences for each woman,
# find a stable matching between the men and women
def gale_shapley(mprefs, wprefs):
	# gale_shapley(mprefs, wprefs) => matching
	# mprefs[m] is the list of man m's preferences
	# wprefs[w] is the list of woman w's preferences	
	# matching[w] is the man that woman w has accepted
	matching = [None] * len(wprefs)
	
	# if next_woman[m] = w, then 
	# man m proposes to the wth woman on his list next
	# initially each man proposes to the zeroth (first) woman on his list
	next_woman = [0] * len(mprefs)
	
	# initially every man is unengaged
	unengaged_men = range(len(mprefs))
	
	# until every man is engaged, each unengaged man proposes to the next woman on his list
	# if the woman is unmatched, match her with the unengaged man
	# if she is matched but prefers the unengaged man to her fiance,
	# match her with the unengaged man and make her fiance unengaged
	while unengaged_men:
		man = unengaged_men.pop(0)
		woman = mprefs[man][next_woman[man]]
		next_woman[man] += 1
		if matching[woman]:
			if wprefs.index(man) < wprefs.index(matching[woman]):				
				unengaged_men.append(matching[woman])
				matching[woman] = man
			else: unengaged_men.append(man)
		else: matching[woman] = man

	return matching
	
print gale_shapley([[0, 1, 2], [2, 1, 0], [1, 0, 2]], [[1, 2, 0], [2, 1, 0], [0, 1, 2]])
