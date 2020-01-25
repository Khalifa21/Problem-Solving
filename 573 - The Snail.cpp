#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	int H,U,D,F,count;
	double sum;
	double fatigue;
	double UU;
	scanf("%d %d %d %d",&H,&U,&D,&F);	
	bool check;
	while(H != 0){
		sum = 0.0;
		fatigue = F/100.0 * U;
		count = 1;
		UU = U;
		while (true){ 
		if (count != 1) UU -= fatigue;
		if (UU > 0 ) sum += UU; 
		if (sum > H) {check = true; break;}
		sum -= D; 
		if (sum < 0) {check = false; break;}
		count++;
		}
		if (check) printf("success on day %d\n",count);
		else printf("failure on day %d\n",count);
		scanf("%d %d %d %d",&H,&U,&D,&F);	
	}
	return 0;
}