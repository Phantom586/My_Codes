#include<stdio.h>
#include<conio.h>
#include<conio.h>
int front=-1,rear=-1;
int arr[10];
int max=10;
void Insert(int item){
	if(front == 0 && rear == max-1){
		printf("\nQueue Full");
	}
	else if(rear == -1){
		front = 0;
		rear = 0;
		arr[rear] = item;
	}
	else{
		rear++;
		arr[rear] = item;
	}
}
void Delete(){
	if(front == rear){
		printf("\nQueue will be Empty");
		fflush(stdin);
		printf("\nDo you Still Want to Delete it ?  : Y or N");
		char c = getchar();
		if(c == 'Y'|| c== 'y')
			goto x;
	}
	else if(rear == 0){
		printf("\nQueue Empty");
	}
	else{
		x:
		int ditem = arr[front];
		printf("\n Dequeued Item is : %d",ditem);
		front++;
	}
}
void Display(){
	int i;
	printf("\nQueue Now :");
	for(i=front;i<=rear;i++)
	printf(" %d",arr[i]);
}
main(){
	char ch1;
	int item;
	do{
		int ch;
		printf("\nSelect Operation :");
		printf("\nPress 1 for Inserting an Element :");
		printf("\nPress 2 for Deleting an Element :");
		scanf("%d",&ch);
		if(ch==1){
			printf("\nEnter the Data :");
			scanf("%d",&item);
			Insert(item);
			Display();
		}
		else if(ch==2){
			Delete();
			Display();
		}
		fflush(stdin);
		printf("\nContinue : Y or N\n");
		ch1=getchar();
	}while(ch1=='y'||ch1=='Y');
	printf("\n%d %d",front,rear);
}
