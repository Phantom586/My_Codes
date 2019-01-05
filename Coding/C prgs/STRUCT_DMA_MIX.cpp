#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>
typedef struct STUDENT{
	char name[20];
	int roll,marks;
}stud;
main(){
	stud f[20],*ptr;
	char ch;
	int n,i,j,m=0,k;
	printf("Enter the Number of Records :");
	scanf("%d",&n);
	ptr=(stud*)calloc(n,sizeof(stud));
	if(ptr==NULL){
		printf("Couldn't Create Memory :");
		exit(1);
	}
	else{
		for(i=0;i<n;i++){
			fflush(stdin);
			printf("\nEnter the %d name :",(i+1));
			gets((ptr+i)->name);
			printf("\nEnter the Roll no :");
			scanf("%d",&(ptr+i)->roll);
			printf("\nEnter the Marks :");
			scanf("%d",&(ptr+i)->marks);
		}
		fflush(stdin);
		printf("\nDo you want to Enter more Names : Y");
		scanf("%c",&ch);
		if(ch=='Y' || ch=='y'){
			printf("\nHow Many :");
			scanf("%d",&m);
			ptr=(stud*)realloc(ptr,(m+n)*sizeof(stud));
			for(i=n;i<(m+n);i++){
				fflush(stdin);
				printf("\nEnter the %d name :",(i+1));
				gets((ptr+i)->name);
				printf("\nEnter the Roll no :");
				scanf("%d",&(ptr+i)->roll);
				printf("\nEnter the Marks :");
				scanf("%d",&(ptr+i)->marks);
			}
		}
		for(i=0;i<(n+m);i++){
			printf("\n====================");
			printf("\n%s\t%d\t%d",(ptr+i)->name,(ptr+i)->roll,(ptr+i)->marks);
		}
		
	}
	free(ptr);
}
