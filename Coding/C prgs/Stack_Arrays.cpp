#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int top=-1,arr[100];
void display(){
	printf("\n\nElements in the Stack are :");
	for(int i=0;i<=top;i++){
		printf("%d",arr[i]);
	}
}
int push(int n){
	if(n==top){
		printf("\n*******Overflow********");
		display();
	}
	else{
		scanf("%d",&arr[top]);
	}
}
int pop(){
	if(top==-1){
		printf("\n******Underflow*******");
		display();
	}
	else{
		printf("\nThe Popped Element is : %d",arr[top]);
		arr[top--]=0;
		display();
	}
}
int main(){
	int ch,n;
	char ch1;
	puts("Enter the Size of the Array :");
	scanf("%d",&n);
	while(1){
		printf("\n\nPress 1 for Inserting an element :");
		printf("\nPress 2 for Deleting an element :");
		printf("\nPress 3 for Displaying the Stack :");
		printf("\nPress 4 to Exit :");
		scanf("%d",&ch);
		if(ch==1){
			printf("\nEnter the Data :");
			top++;
			push(n);
		}
		else if(ch==2){
			pop();
		}
		else if(ch==3){
			display();
		}
		else if(ch==4){
			display();
			exit(0);
		}
		else{
			puts("\nInvalid Choice !!");
		}
	}
}
