#include<stdio.h>
#include<string.h>
main()
{
	char a[20],c;
	int i,j,n,count=0;
	puts("Enter a String");
	gets(a);
	n=strlen(a);
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){ 
			if(i!=j){
				if(a[i]==a[j]){
					count++;
					c=a[i];
					puts("Recurring Character Found !");
					goto x;
				}
			}
		}
	}
	x:
		if(count!=0)
		{
		printf("The First Recurring Character is %c",c);
		}
		else
		printf("NULL");
}
