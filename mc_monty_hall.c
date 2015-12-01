#include <time.h>   // to seed the rng
#include <stdlib.h> // srand(), rand()
#include <stdio.h>  // printf

int main()
{
	const int NUM_DOORS = 3;
	const int NUM_SIMS = 100000;
	int prize, choice, goat, change, i;
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

		// locate other door
    		for (change = 0; change == goat || change == choice; change++);

		// compute wins
		if (choice == prize)
      			stay_wins++;
    		else if (change == prize)
      			change_wins++;
	}

	printf("%f\n", (1.0 * stay_wins / NUM_SIMS) * 100);
	printf("%f\n", (1.0 * change_wins / NUM_SIMS) * 100);
  
  	return 0;
}
