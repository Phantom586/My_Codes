#include<stdio.h>
main(){
	char arr[20];
	scanf("%[^\n]c",&arr);
	for(int i=0;i<20;i++)
	printf("%c",arr[i]);
}
