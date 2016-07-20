#include <time.h>   // to seed the rng
#include <stdlib.h> // srand(), rand()
#include <stdio.h>  // printf

int main()
{
	const int NUM_DOORS = 3;
	const int NUM_SIMS = 100000;
	int prize, choice, goat, remaining, i;
	int stay_wins = 0, change_wins = 0;

	srand(time(NULL));

	for (i = 0; i < NUM_SIMS; i++)
	{
		// determine prize door
		prize = rand() % NUM_DOORS;
        
		// contestant picks a door
		choice = rand() % NUM_DOORS;

		// host opens a door to reveal a goat
		do {
			goat = rand() % NUM_DOORS;
		} while (goat == prize || goat == choice);

		// locate remaining door
    		for (remaining = 0; remaining == goat || remaining == choice; remaining++);

		// compute wins
		if (choice == prize)
      			stay_wins++;
    		else if (remaining == prize)
      			change_wins++;
	}

	// report wins
	printf("%f\n", (1.0 * stay_wins / NUM_SIMS) * 100);
	printf("%f\n", (1.0 * change_wins / NUM_SIMS) * 100);
  
  	return 0;
}
