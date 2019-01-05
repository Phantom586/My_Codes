#include<stdio.h>
#include<string.h>
int main()
{
	int i,x[20],n;
	puts("Enter your Digit :");
	scanf("%d",&n);
	for(i=0;n>0;i++){
		x[i]=n%2;
		n=n/2;
	}
	puts("The Binary Equivalent is :");
	for(i=i-1;i>=0;i--){
		printf("%d",x[i]);
	}
	return 0;
}
