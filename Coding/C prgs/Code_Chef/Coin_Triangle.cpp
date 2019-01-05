#include<stdio.h>
#include<string.h>
main(){
	int num,i,c,t;
	puts("No. of Test Cases :");
	scanf("%d",&t);
	while(t--){
		c=0;
		scanf("%d",&num);
		for(i=1;i<=num;i++){
			c++;
			num=num-i;
		}
		printf("%d \n",c);
	}
}
