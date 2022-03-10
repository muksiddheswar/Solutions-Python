#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;


int main()
{
	int n, q, i, size, j, value, a, b;
	vector<vector<int>> nvec;

	scanf("%d %d", &n, &q);
	
	for(i=0; i<n; ++i)
	{
		vector<int> ivec;
		scanf("%d", &size);
		for(j=0; j<size; ++j)
		{
			scanf("%d", &value);
			ivec.push_back(value);
		}
		nvec.push_back(ivec);
	}
	
	for(i=0; i<q; ++i)
	{
		scanf("%d %d", &a, &b);
		printf("%d \n", nvec[a][b]);
	}

	return 0;
}