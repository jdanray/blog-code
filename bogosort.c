#include <time.h>
#include <stdlib.h>

int main() {
   	srand(time(NULL));
	int arr[2] = {3,1};
	int order[2] = {1,3};
	int len = sizeof(arr) / sizeof(arr[0]);
	while (arr != order) 
	{
		//Shuffle
		for (int i = len - 1; i > 0; i--) 
		{
			int temp = arr[i];
			int r = rand() % (i + 1);
			arr[i] = arr[r];
			arr[r] = temp;
		}
	} 
}
