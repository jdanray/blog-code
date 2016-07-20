#include <cstdlib>		// rand(), atoi()
#include <iostream>		// cout, cerr
#include <time.h>		// to seed rand()

using namespace std;

int* simulate_seating(int num_passengers, int num_simulations)
{
	int i, j, r;

	// got_seat[i] is the number of times that passenger i got their assigned seat
	int* got_seat = new int[num_passengers];
	for (i = 0; i < num_passengers; i++)
		got_seat[i] = 0;

	// assigned[i] is the seat that passenger i is assigned to
	int* assigned = new int[num_passengers];

	// prev_assigned[i] is true iff seat i has already been assigned to a passenger
	bool* prev_assigned = new bool[num_passengers];

	// occupied[i] is true iff seat i is occupied
	bool* occupied = new bool[num_passengers];

	// seed rand()
	srand(time(NULL));

	// start the simulation
	for (i = 0; i < num_simulations; i++)
	{
		// initially, nobody has been assigned a seat
		for (j = 0; j < num_passengers; j++)
			prev_assigned[j] = false;

    		// assign everyone a seat at random
		for (j = 0; j < num_passengers; j++)
		{
			// make sure the seat hasn't already been assigned
			do {
				r = rand() % num_passengers;
			} while (prev_assigned[r]);

			// make the assignment
			prev_assigned[r] = true;
			assigned[j] = r;
		}
	
		// initially, nobody is occupying any seat
		for (j = 0; j < num_passengers; j++)
			occupied[j] = false;

		// the first passenger takes a seat at random
		r = rand() % num_passengers;
		occupied[r] = true;
		if (r == assigned[0])
			got_seat[0]++;

		// the rest of the passengers try to sit in their assigned seats
		// if their seat is occupied, they take a seat at random
		for (j = 1; j < num_passengers; j++)
		{
			if (!occupied[assigned[j]])
			{
				occupied[assigned[j]] = true;
				got_seat[j]++;
			} else {
				// because a passenger picks a seat at random,
				// that seat might already be occupied
				// so, try until you find an unoccupied one
				do {
					r = rand() % num_passengers;
				} while (occupied[r]);

                                // occupy the seat
				occupied[r] = true;
			}
		}
	}

	// clean up
	delete[] occupied;
	delete[] assigned;
	//delete[] got_seat;

	return got_seat;
}

void display(int* got_seat, int num_passengers, int num_simulations)
{
	int i, k;
	
	for (i = 0; i < num_passengers; i++)
	{
                // display results
                k = i + 1;
		cout << "Passenger #" << k << " got their assigned seat " << got_seat[i] << " out of ";
		cout << num_simulations << " (" << 100.0 * got_seat[i] / num_simulations << "%) times.";
            
                // display exact probabilities
                // for k = 1, the probability that passenger k gets their assigned seat is 1/n
                // for 2 <= k <= n, the probability that passenger k gets their assigned seat is 1 - 1/(n + 2 - k)
                cout << " (Exact probability: "; 
                if (k == 1)
                    cout << (1.0 / num_passengers) * 100;
                else
                    cout << (1 - 1.0 / (num_passengers + 2 - k)) * 100;
                cout << "%)" << endl;
	}
}

int main(int argc, char** argv)
{
	if (argc != 3)
	{
		cerr << "usage: " << argv[0] << " <# passengers> <# simulations>" << endl;
		return -1;
	}
	
	int num_passengers = atoi(argv[1]);
	int num_simulations = atoi(argv[2]);
	
	if (num_passengers <= 0 || num_simulations <= 0)
	{
		cerr << "Input values should be integers and greater than zero." << endl;
		return -1;
	}

	display(simulate_seating(num_passengers, num_simulations), num_passengers, num_simulations);

	return 0;
}
