// https://icpcarchive.ecs.baylor.edu/external/75/7513.pdf

#include <iostream>

using namespace std;

int main()
{
  int num_problems;
	cin >> num_problems;
	
	int** best_poster = new int*[num_problems];
	
	for (int i = 0; i < num_problems; i++)
	{
	
		int num_billboards;
		cin >> num_billboards;
		
		int** billboards = new int*[num_billboards];
		
		int max_width = 0;
		int max_height = 0;
		
		for (int j = 0; j < num_billboards; j++)
		{
			int w, h;
			cin >> w >> h;
		
			billboards[j] = new int[2];
			billboards[j][0] = w;
			billboards[j][1] = h;
			
			if (w > max_width)
			{
				max_width = w;
			}
			if (h > max_height)
			{
				max_height = h;
			}
		}
		
		int max_total_area = 0;
		best_poster[i] = new int[2];
		for (int w = 1; w <= max_width; w++)
		{
			for (int h = 1; h <= max_height; h++)
			{
				int num_posters = 0;
				for (int i = 0; i < num_billboards; i++)
				{
					if (w <= billboards[i][0] && h <= billboards[i][1])
					{
						num_posters++;
					}
				}

				int total_area = w * h * num_posters;
				if (total_area > max_total_area)
				{
					max_total_area = total_area;
					best_poster[i][0] = w;
					best_poster[i][1] = h;
				}
			}
		}
		
		delete[] billboards;		
	}
	
	for (int i = 0; i < num_problems; i++)
	{
		cout << best_poster[i][0] << " " << best_poster[i][1] << endl;	
	}
	
	delete[] best_poster;

	return 0;
}
