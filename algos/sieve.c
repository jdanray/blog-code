#include <stdlib.h>
#include <stdio.h>

void prime_list(int N, int* is_prime) {
	int  i;
	int  j;
	
        // initialize all numbers as prime
	for (i = 0; i <= N; i++) {
		is_prime[i] = 1;
	}
	
        // starting with i=2, 
        // process all numbers i<sqrt(N)
	i = 2;
	while (i * i <= N) {
                // mark all multiples of i as composite
		for (j = 2; j <= N / i; j++) {
			is_prime[j * i] = 0;
		}
		
                // go to the next prime number
                // while the current number is composite,
                // try the next number in sequence
		do {
			i++;
		} while (!is_prime[i]);
	}
}

int main() {
	int* is_prime;
	int  i;
	int  N;
	
	N = 21;
	is_prime = (int*) malloc(sizeof(int) * (N + 1));

	prime_list(N, is_prime);
	
	for (i = 2; i <= N; i++) {
		if (is_prime[i]) {
			printf("%i\n", i);
		}
	}
	
	free(is_prime);

	return 0;
}
