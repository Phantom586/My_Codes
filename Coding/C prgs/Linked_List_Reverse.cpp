#include<stdio.h>
#include<malloc.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
typedef struct node{
	int data;
	struct node *next;
}node;
node* getNode(){
	node *ptr;
	ptr = (node*)malloc(sizeof(node));
	return ptr;
}
main(){
	node *ptr,*start,*first=NULL,*ctr;
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
		if(first==NULL){
			start=first=ptr;
		}
		else{
			start->next=ptr;
			start=ptr;
		}
		puts("\nContinue : Y or N");
		choice = getch();
	}while(choice == 'Y'|| choice=='y');
	ptr = first;
	if(count > 0){
		puts("\n\nThe Linked List is :");
		while(ptr!=NULL){
			printf("%d =>",ptr->data);
			ptr=ptr->next;
		}
		printf("NULL");
	}
	puts("\nThe Reversed Linked List is :");
	node *prev = NULL;
	ptr = first;
	ctr = first->next;
	while(ctr != NULL){
		ptr->next = prev;
		prev = ptr;
		ptr = ctr;
		ctr = ptr->next;
	}
	ptr->next = prev;
	first = ptr;
	ptr = first;
	while(ptr!=NULL){
			printf("%d =>",ptr->data);
			ptr=ptr->next;
		}
		printf("NULL");
}
