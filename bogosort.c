#include <time.h>
#include <stdlib.h>

void shuffle(int*& arr)
{
    int len = sizeof(arr) / sizeof(arr[0]);
	
    if (len > 1) 
    {
        for (int i = len - 1; i > 0; i--) 
        {
            int temp = arr[i];
            int r = rand() % (len + 1);
            arr[i] = arr[r];
            arr[r] = temp;
        }        
    }
}

void bogosort(int*& arr, int* order)
{
  while (arr != order) 
	{
    shuffle(arr);
	}
}
