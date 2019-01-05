#include<stdio.h>
#include<malloc.h>
#include<string.h>
main(){
	char *str1,*str2,*str3,temp[30];
	int k,l,m,n;
	puts("Enter the Length of the First String :");
	scanf("%d",&k);
	puts("Enter the Length of the First String :");
	scanf("%d",&l);
	str1=(char*)malloc(n*sizeof(char));
	str2=(char*)malloc(n*sizeof(char));
	if(str1==NULL || str2==NULL){
		puts("Problem Occurred !!");
		
	}
	else{
		fflush(stdin);
		puts("Enter the First String :");
		gets(str1);
		puts("Enter the Second String :");
		gets(str2);
		puts("Enter The Changes to be Made :");
		scanf("%d %d",&m,&n);
		int c=0,j=0;
		for(int i=0;*(str1+i)!='\0';i++){
			if(*(str1+i)==' ')
			c++;
			if(c==(m-1)){
				temp[j++]=*(str1+i);
			}
		}
		puts(temp);
	}
}
