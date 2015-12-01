#include <time.h>   // to seed rng
#include <stdlib.h> // srand(), rand()
#include <stdio.h>

int main()
{
	const int NUM_DOORS = 3;
	const int NUM_SIMS = 100000;
	int prize, choice, goat, switch_door, i;
	int stay_wins = 0, switch_wins = 0;

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

		do goat = rand() % NUM_DOORS; while (goat == prize || goat == choice);


		// locate other door
    		for (switch_door = 0; switch_door == goat || switch_door == choice; switch_door++);

		// compute wins
		if (choice == prize)
      			stay_wins++;
    		else if (switch_door == prize)
      			switch_wins++;
	}

	printf("%f\n", (1.0 * stay_wins / NUM_SIMS) * 100);
	printf("%f\n", (1.0 * switch_wins / NUM_SIMS) * 100);
  
  	return 0;
}
