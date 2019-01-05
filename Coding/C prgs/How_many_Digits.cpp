#include<stdio.h>
#include<string.h>
void Digits(long n){
	int i=0;
	while(n!=0){
		i++;
		n=n/10;
	}
	if(i>3)
	printf("More than 3 digits");
	else
	printf("%d\n",i);
}
int main(){
	int t;
	long n;
	scanf("%d",&t);
	while(t--){
		scanf("%ld",&n);
		if(n>=0 && n<=1000000)
		Digits(n);
	}
	return 0;
}
