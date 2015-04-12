import random

# given an integer n>1,
# returns integers k and q such that (2^k)q = n,
# where k>0 and q is odd
def kq(n):
	q = n / 2
	k = 1
	while q % 2 == 0:
		q /= 2
		k += 1
	return k, q

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
	elif n % 2 == 0:
		return False
	k, q = kq(n - 1)
	a = random.randint(2, n - 2) # 1 < a < n-1
	if (a ** q) % n == 1: 
		return True
	for j in range(k):
		if (a ** ((2 ** j) * q)) % n == n - 1: 
			return True
	return False
