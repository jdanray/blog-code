#include <stdlib.h>
#include <stdio.h>

// the sieve of Erastosthenes

void sieve(int N, int* is_prime) {
	int  i;
	int  j;
	
        // initialize all numbers as prime
	for (i = 0; i <= N; i++) {
		is_prime[i] = 1;
	}
	
        // remove all composite numbers
	i = 2;
	while (i * i <= N) {
                // mark all multiples of i as composite
		for (j = 2; j <= N / i; j++) {
			is_prime[j * i] = 0;
		}
		
                // go to the next prime number
		do {
			i++;
		} while (!is_prime[i]);
	}
}

int main(int argc, char* argv[]) {
	int*  is_prime;
	int   i;
	long  N;
	char* p;

	// define N
	if (argc > 1) {
		N = strtol(argv[1], &p, 10);
	} else {
		N = 100;
	}

	// find all prime numbers from 2 to N
	is_prime = (int*) malloc(sizeof(int) * (N + 1));
	sieve(N, is_prime);

	// report results
	for (i = 2; i <= N; i++) {
		if (is_prime[i]) {
			printf("%i ", i);
		}
	}
	printf("\n");
	
	free(is_prime);
	return 0;
}
