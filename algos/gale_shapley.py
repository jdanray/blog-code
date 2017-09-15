# given preferences for each man and preferences for each woman,
# find a stable matching between the men and women
def gale_shapley(mprefs, wprefs):
	# test whether there are as many men as women
	assert(len(mprefs) == len(wprefs))

	# wprefs[i] is the list of woman i's preferences
	# e.g., if wprefs[0] == [0, 1, 2], then
	# woman 0's preferences are: man 0 > man 1 > man 2
	# matching[i] is the man that woman i has accepted
	N = len(wprefs)
	matching = [None] * N

	# if wrank[i][j] == k, then
	# man j is woman i's k-th choice
	wrank = [[None] * N for _ in range(N)]
	for i, wp in enumerate(wprefs):
		for k, j in enumerate(wp):
			wrank[i][j] = k

	# if next_woman[i] == j, then 
	# man i proposes to the j-th woman on his list next
	# initially each man proposes to the zeroth (first) woman on his list
	next_woman = [0] * N

	# initially every man is unengaged
	# until every man is engaged, each unengaged man proposes to the next woman on his list
	# if the woman is unmatched, match her with the unengaged man
	# if she is matched but prefers the unengaged man to her fiance,
	# match her with the unengaged man and make her fiance unengaged
	# if neither, the man remains unengaged and moves onto the next woman
	unengaged_men = list(range(N))
	while unengaged_men:
		man = unengaged_men.pop(0)
		woman = mprefs[man][next_woman[man]]
		next_woman[man] += 1
		fiance = matching[woman]
		if fiance == None:
			matching[woman] = man
		elif wrank[woman][man] < wrank[woman][fiance]:
			matching[woman] = man
			unengaged_men.append(fiance)
		else:
			unengaged_men.append(man)

	return matching

mprefs = [[0, 1], [0, 1]]
wprefs = [[0, 1], [0, 1]]
print(gale_shapley(mprefs, wprefs)) # output: [0, 1]
