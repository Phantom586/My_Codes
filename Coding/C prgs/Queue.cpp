#include<stdio.h>
#include<conio.h>
#include<conio.h>
int front=-1,rear=-1;
int arr[10];
int max=10;
void Insert(){
	if(rear==max){
		printf("\nQueue Full");
		printf("\n%d %d",front,rear);
	}
	else if(front==rear){
		front=-1;
		rear=0;
		scanf("%d",&arr[rear]);
	}
	else{
		rear++;
		scanf("%d",&arr[rear]);
		printf("\n%d %d",front,rear);
	}
}
void Delete(){
	if(front==rear){
		printf("\nQueue Empty");
		front=-1;
		rear=-1;
		printf("\n%d %d",front,rear);
	}
	else{
		front++;
		arr[front]=0;
		printf("\n%d %d",front,rear);
	}
}
void display(){
	for(int i=(front+1);i<=rear;i++)
	printf("%d",arr[i]);
}
main(){
	char ch1;
	do{
		int ch;
		printf("\nSelect Operation :");
		printf("\nPress 1 for Inserting an Element :");
		printf("\nPress 2 for Deleting an Element :");
		scanf("%d",&ch);
		if(ch==1){
			Insert();
			printf("\nQueue After Insertion is :");
			display();
		}
		else if(ch==2){
			Delete();
			printf("\nQueue After Deletion is :");
			display();
		}
		fflush(stdin);
		printf("\nContinue : Y or N");
		ch1=getchar();
	}while(ch1=='y'||ch1=='Y');
	printf("\n%d %d",front,rear);
}
