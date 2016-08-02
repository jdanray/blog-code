#include <stdlib.h>
#include <stdio.h>

void small_prime_list(int n, int* b) {
	int  i;
	int  j;
	
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
}

int main() {
	int* b;
	int  i;
	int  n;
	
	n = 11;
	b = (int*) malloc(sizeof(int) * (n + 1));

	small_prime_list(n, b);
	
	for (i = 0; i <= n; i++) {
		if (b[i]) {
			printf("%i\n", i);
		}
	}
	
	free(b);

	return 0;
}
