#include<stdio.h>
#include<string.h>
typedef struct student{
	char name[20];
	int roll,m1,m2;
}stud;
main(){
	stud f[20];
	int i,j,n,loc1=0,loc2=0,max1,max2;
	puts("Enter the No. of Records you want to Store :");
	scanf("%d",&n);
	for(i=0;i<n;i++){
		fflush(stdin);
		printf("\nEnter the %d Name :",(i+1));
		gets(f[i].name);
		printf("\nEnter the %d Roll no :",(i+1));
		scanf("%d",&f[i].roll);
		puts("\nEnter the Maths Marks:");
		scanf("%d",&f[i].m1);
		puts("\nEnter the Physics Marks:");
		scanf("%d",&f[i].m2);
	}
	max1=f[0].m1;
	max2=f[0].m2;
	for(j=0;i<n;j++){
		if(f[j].m1>max1){
			max1=f[j].m1;
			loc1=j;		
		}
	}
	for(j=0;i<n;j++){
		if(f[j].m2>max2){
			max2=f[j].m2;
			loc2=j;		
		}
	}
	puts("\n-----------------");
	printf("\nThe Topper of Math is : %s",f[loc1].name);
	printf("\nRoll no : %d",f[loc1].roll);
	printf("\nMarks 1 : %d",f[loc1].m1);
	printf("\nMarks 2 : %d",f[loc1].m2);
	puts("\n-----------------");
	printf("\nThe Topper of Physics is : %s",f[loc2].name);
	printf("\nRoll no : %d",f[loc2].roll);
	printf("\nMarks 1 : %d",f[loc2].m1);
	printf("\nMarks 2 : %d",f[loc2].m2);
	
}
