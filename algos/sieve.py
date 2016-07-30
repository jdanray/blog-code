# the sieve of eratosthenes

def small_prime_list(n):
	assert 2 <= n <= 2 ** 20
	
	b = dict((i, True) for i in range(2, n + 1))
	
	i = 2
	while i ** 2 <= n:
		for j in range(2, (n // i) + 1):
			b[j * i] = False
		
		i += 1
		while not b[i]:
			i += 1
			
	primes = [k for k in b if b[k]]
	return primes
