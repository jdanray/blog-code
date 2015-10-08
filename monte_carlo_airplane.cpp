#include <cstdlib>		// rand(), atoi()
#include <iostream>		// cout, cerr
#include <time.h>		// to seed rand()

using namespace std;

int main(int argc, char** argv)
{
	// arg check
	if (argc != 3)
	{
		cerr << "usage: " << argv[0] << " <# passengers> <# simulations>" << endl;
		return -1;
	}
	
	int n = atoi(argv[1]);
	int num_simulations = atoi(argv[2]);
	
	if (n <= 0 || num_simulations <= 0)
	{
		cerr << "Input values should be integers and greater than zero." << endl;
		return -1;
	}
	
	// support vars
	int i, j, r, k;

	// got_seat[i] is the number of times that passenger i got their assigned seat
	// so, if got_seat[2] == 531, then passenger #2 got their assigned seat 531 times
	int* got_seat = new int[n];
	for (i = 0; i < n; i++)
		got_seat[i] = 0;

	// assigned[i] is the seat that passenger i is assigned to
	// so, if assigned[2] == 5, then passenger #2 is assigned to seat #5
	int* assigned = new int[n];

	// prev_assigned[i] is true iff seat i has already been assigned to a passenger
	// so, if prev_assigned[2] == true, then seat #2 has already been assigned
	bool* prev_assigned = new bool[n];

	// occupied[i] is true iff seat i is occupied
	// so, if occupied[2] == true, then seat #2 is occupied
	bool* occupied = new bool[n];

	// seed rand()
	srand(time(NULL));

	// start the simulation
	for (i = 0; i < num_simulations; i++)
	{
		// initially, nobody has been assigned a seat
		for (j = 0; j < n; j++)
			prev_assigned[j] = false;

    		// assign everyone a seat at random
		for (j = 0; j < n; j++)
		{
			// make sure the seat hasn't already been assigned
			r = rand() % n;
			while (prev_assigned[r])
				r = rand() % n;

			// make the assignment
			prev_assigned[r] = true;
			assigned[j] = r;
		}
	
		// initially, nobody is occupying any seat
		for (j = 0; j < n; j++)
			occupied[j] = false;

		// the first passenger takes a seat at random
		r = rand() % n;
		occupied[r] = true;
		if (r == assigned[0])
			got_seat[0]++;

		// the rest of the passengers try to sit in their assigned seats
		// if their seat is occupied, they take a seat at random
		for (j = 1; j < n; j++)
		{
			if (!occupied[assigned[j]])
			{
				occupied[assigned[j]] = true;
				got_seat[j]++;
			} else {
				// because a passenger picks a seat at random,
				// that seat might already be occupied
				// so, try until you find an unoccupied one
				r = rand() % n;
				while (occupied[r])
					r = rand() % n;

                                // occupy the seat
				occupied[r] = true;
			}
		}
	}

	// print output
	for (i = 0; i < n; i++)
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
                    cout << (1.0 / n) * 100;
                else
                    cout << (1 - 1.0 / (n + 2 - k)) * 100;
                cout << "%)" << endl;
	}

	// clean up
	delete[] occupied;
	delete[] assigned;
	delete[] got_seat;

	return 0;
}
