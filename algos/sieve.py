def small_prime_list(n):
	# n must be greater than 1
	# but more than 2 ** 20 is too computationally demanding
	assert 2 <= n <= 2 ** 20	
	
	# construct all the integers from 2 to n
	# tag them all as prime initially
	b = dict((i, True) for i in range(2, n + 1))
	
	# iteratively untag the composite numbers
	# every composite number k has at least one prime factor less than or equal to sqrt(k)
	# so, to untag all the composite numbers from 2 to n, 
	# take all the prime numbers from 2 to sqrt(n), and untag all of their multiples
	i = 2
	rt = n ** 0.5
	while i <= rt:
		# untag all of the multiples of i from 2i, 3i, ..., (n/i)i
		for j in range(2, (n // i) + 1):
			b[j * i] = False
		
		# go to the next smallest prime number
		i += 1
		while not b[i]:
			i += 1

	primes = [k for k in b if b[k]]
	return primes
