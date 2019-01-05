#include<stdio.h>
main(){
	int n,i,c=0;
	printf("Enter the Number :");
	scanf("%d",&n);
	for(i=2;i<n/2;i++){
		if(n%i == 0)
			c++;
	}
	if(c == 0 )
		printf("Prime");
	else
		printf("Not Prime");
}
