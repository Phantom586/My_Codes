#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
typedef struct node{
	int data;
	struct node *next;
}node;


node *front = NULL,*rear = NULL,*ctr=NULL;

node* getNode(){
	node *ptr = (node*)malloc(sizeof(node));
	ptr->next=NULL;
	return ptr;	
}

void Insert(node *ptr,int item){
	if(ptr == NULL){
		printf("\n Queue Overflow :");
	}
	else if(ctr == NULL){
		front = ptr;
		rear = ptr;
		ptr->data = item;
		ctr = ptr;
	}
	else{
		ctr->next=ptr;
		ptr->data = item;
		ctr = ptr;
		rear = ptr;	
	}
}

void Delete(){
	if(front == NULL){
		printf("\nQueue Underflow :");
	}
	else if(front == rear){
		printf("\nQueue will be Empty :");
		fflush(stdin);
		printf("\nDo you Still want to Continue : Y or N");
		char c = getchar();
		if(c=='y'||c=='Y'){
			node *nex;
			nex=front;
			int item = front->data;
			printf("\nDequeued Item is : %d",item);
			front = front->next;
			free(nex);
			rear = ctr = NULL;
		}
			
	}
	else{
		node *nex;
		nex=front;
		int item = front->data;
		printf("\nDequeued Item is : %d",item);
		front = front->next;
		free(nex);	
	}
}

void Display(){
	node *nex;
	nex = front; 
	printf("\nQueue Now :");
	while(nex != NULL){
		printf(" %d",nex->data);
		nex = nex->next;
	}
}

main(){
	node *ptr;
	char ch1;
	int item;
	do{
		int ch;
		printf("\nSelect Operation :");
		printf("\nPress 1 for Inserting an Element :");
		printf("\nPress 2 for Deleting an Element :");
		scanf("%d",&ch);
		if(ch==1){
			ptr = getNode();
			printf("\nEnter the Data :");
			scanf("%d",&item);
			Insert(ptr,item);
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
}
