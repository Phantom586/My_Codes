#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
int top=-1,n=10;
typedef struct node{
	int data;
	struct node *next,*prev;
}node;
node *ptr,*head=NULL,*ctr,*last;
node* getNode(){
	node *ptr;
	ptr=(node*)malloc(sizeof(node));
	return ptr;
}
void display(){
	ptr=last;
	printf("\nStack Now :");
	printf("\n--------");
		while(ptr!=NULL){
			printf("\n   %d",ptr->data);
			printf("\n--------");
			ptr=ptr->prev;
		}
}
int push(){
	if(n==top){
		printf("\n*******Overflow********");
	}
	else{
		ptr=getNode();
		printf("\nEnter the Data :");
		scanf("%d",&ptr->data);
		ptr->next=NULL;
		if(head==NULL){
			ptr->prev=NULL;
			ctr=head=ptr;
		}
		else{
			ctr->next=ptr;
			ptr->prev=ctr;
			ctr=last=ptr;
		}
	}
}
int pop(){
	char ch1;
	if(top==-1){
		printf("\n******Underflow*******");
		display();
	}
	else{
		if(head==last){
			printf("\nAre u Sure : Y or N");
			ch1=getch();
			if(ch1=='y'||ch1=='Y'){
				printf("\nThe Last Element of the Stack is : %d",last->data);
				top--;
				node *nex;
				nex=last->prev;
				nex->next=NULL;
				free(last);
				last=nex;
				printf("\nSatck Empty__$___");
				display();
			}
			else
				exit(0);
		}
		else{
			printf("\nThe Popped Element is : %d",last->data);
			top--;
			node *nex;
			nex=last->prev;
			nex->next=NULL;
			free(last);
			last=nex;
			display();	
		}
	}
}
main(){
	int ch;
	char ch1;
	while(1){
		printf("\n\nPress 1 for Inserting an element :");
		printf("\nPress 2 for Deleting an element :");
		printf("\nPress 3 for Displaying the Stack :");
		printf("\nPress 4 to Exit :");
		scanf("%d",&ch);
		if(ch==1){
			top++;
			push();
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
