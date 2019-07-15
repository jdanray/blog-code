from random import shuffle

def test(sort, n=1000, ntries=1000):
	touchstone = list(range(n))
	dice = list(touchstone)
	for _ in range(ntries):
		shuffle(dice)
		assert(sort(dice) == touchstone)
