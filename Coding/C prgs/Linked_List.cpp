#include<stdio.h>
#include<malloc.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
typedef struct node{
	int data;
	struct node *next;
}node;
main(){
	node *ptr,*start,*first=NULL;
	char choice;
	int count=0;
	do{
		ptr=(node*)malloc(sizeof(node));
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
}
