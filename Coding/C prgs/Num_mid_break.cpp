#include<stdio.h>
#include<string.h>
main(){
	int num,i=0,j,m,temp,d,a[10];
	puts("Enter the number");
	scanf("%d",&num);
	temp=num;
	while(temp!=0){
		i++;
		temp=temp/10;
	}
	m=i;
	for(j=0;j<i;j++){
		d=num%10;
		a[j]=d;
		num=num/10;
	}
	int b[i];
	printf("Index : %d\n",i);
	for(int k=0;k<i;k++){
		b[k]=a[m];
		m--;
	}
	for(int k=0;k<6;k++)
	printf("%d",b[k]);
}
