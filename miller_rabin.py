import random

# given an integer n,
# returns false if n is not prime
# returns true if n is likely prime
def miller_rabin(n):
	# random.randint() will break if n<4
	# so, handle those cases specially
	if n < 2:
		return False
	elif n == 2 or n == 3:
		return True
		
	# no even number >2 is prime
	if n % 2 == 0: 
		return False
		
	# find integers k and q such that (2^k)q = n - 1,
	# where k>0 and q is odd
	q = (n - 1) >> 1 # a right shift is equiv to dividing by 2
	k = 1
	while q % 2 == 0:
		q = q >> 1
		k += 1
	
	# an integer n>3 is prime if,
	# for all 1 < a < n - 1,
	# (a^q) % n = 1 or
	# there exists some 0 <= j < k such that (a^((2^j)*q)) % n = n - 1
	# if n is prime, then one of the conditions holds true for all 1 < a < n - 1
	# so, if it holds true for a random 1 < a < n - 1,
	# then we have evidence that n is prime
	a = random.randint(2, n - 2)
	if (a ** q) % n == 1: 
		return True
	for j in range(k):
		if (a ** ((2 ** j) * q)) % n == n - 1: 
			return True
			
	# neither condition holds true for the random integer
	# we know that n is not prime
	return False
