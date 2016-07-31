#include <stdlib.h>
#include <stdio.h>

int* small_prime_list(int n) {
	int* b;
	int  i;
	int  j;
	
	b = (int*) malloc(sizeof(int) * (n + 1));
	for (i = 0; i <= n; i++) {
		b[i] = 1;
	}
	b[0] = 0;
	b[1] = 0;
	
	i = 2;
	while (i * i <= n) {
		for (j = 2; j <= n / i; j++) {
			b[j * i] = 0;
		}
		
		do {
			i++;
		} while (b[i] == 0);
	}
			
	return b;
}

int main() {
	int* b;
	int  i;
	int  n;
	
	n = 5;
	b = small_prime_list(n);
	
	for (i = 0; i <= n; i++) {
		if (b[i]) {
			printf("%i\n", i);
		}
	}

	return 0;
}
