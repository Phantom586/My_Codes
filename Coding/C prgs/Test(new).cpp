#include<stdio.h>
#include<string.h>
void add(int a[],int n){
	int b[10],c[n+1],sum;
	int carry = 1;
	for(int i=n-1;i>=0;i--){
	sum=a[i]+carry;
	if(sum==10)
	carry=1;
	else
	carry=0;
	b[i]=sum%10;
	}
	if(carry==1){
		c[0]=1;
		goto x;
	}
	for(int i=0;i<n;i++){
		printf("%d",b[i]);
	}
	x:
		for(int i=0;i<n+1;i++)
		printf("%d",c[i]);
}
main()
{
	int a[10],n,i;
	puts("Enter no. of entries in the array");
	scanf("%d",&n);
	printf("Enter :%d Elements in the array ",n);
	for(i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	add(a,n);
}
