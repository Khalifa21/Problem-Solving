#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	int t,n,num,max;
	scanf("%d",&t);	
	for (int i = 0; i < t; ++i)
	{
		scanf("%d",&n);
		max = -1;
		for (int j = 0; j < n; ++j)
		{
			scanf("%d",&num);
			if (num > max) max = num;
		}
		printf("Case %d: %d\n",i+1,max);
	}
	return 0;
}