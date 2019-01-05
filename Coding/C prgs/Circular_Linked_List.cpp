#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
typedef struct node{
	int data;
	struct node *next,*prev;
}node;
node* getNode(){
	node *ptr;
	ptr = (node*)malloc(sizeof(node));
	return ptr;
}
main(){
	node *next,*prev,*head=NULL,*ptr,*ctr,*last;
	char choice;
	int count=0,ch,pos=0;
	do{
		ptr=getNode();
		if(ptr==NULL){
			puts("Some Error Occurred !!");
			exit(0);
		}
		count++;
		printf("\nEnter the Data for :%d node",count);
		scanf("\n%d",&ptr->data);
		ptr->next=NULL;
		if(head==NULL){
			ptr->prev=NULL;
			ctr=head=ptr;
		}
		else{
			ctr->next=ptr;
			ptr->prev=ctr;
			ptr->next=head;
			ctr=last=ptr;
		}
		puts("\nContinue : Y or N");
		choice = getch();
	}while(choice == 'Y'|| choice=='y');
	ptr=head->next;
	if(count > 0){
		printf("\n\nTraversing Circularly Linked List :");
		while(ptr!=head){
			printf("%d <=> ",ptr->data);
			ptr=ptr->next;
		}
		printf("%d",ptr->data);
	}
}
