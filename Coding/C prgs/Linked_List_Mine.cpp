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
	ptr=first;
	printf("\n\n\nSelect Operation to be Performed :");
	printf("\nPress 1 for Inserting a Node at the Beginning of the List :");
	printf("\nPress 2 for Inserting a Node after Kth position in the List :");
	printf("\nPress 3 for Inserting a Node at the End of the List :");
	printf("\n");
	printf("\nPress 4 for Deleting a Node at the Beginning of the List :");
	printf("\nPress 5 for Deleting a Node at Kth Position  of the List :");
	printf("\nPress 6 for Deleting a Node at the End of the List :");
	scanf("%d",&ch);
	//For Inserting a Node at the Beginning of the List
	if(ch==1){
		ctr = getNode();
		printf("Enter the Data for the Node :");
		scanf("%d",&ctr->data);
		ctr->next=first;
		first=ctr;
		ptr=first;
		puts("Linked List Now :");
		while(ptr!=NULL){
			printf("%d => ",ptr->data);
			ptr=ptr->next;
		}
		printf("NULL");
	}
	//For Inserting a Node after Kth position in the List
	else if(ch==2){
		puts("Enter the Position :");
		scanf("%d",&pos);
		int c=0;
		while(ptr!=NULL){
			c++;
			if(c==(pos)){
				ctr=getNode();
				printf("Enter the Data for the Node :");
				scanf("%d",&ctr->data);
				ctr->next=ptr->next;
				ptr->next=ctr;
			}
			ptr=ptr->next;
		}
		ptr=first;
		puts("");
		puts("Linked List Now :");
		while(ptr!=NULL){
			printf("%d => ",ptr->data);
			ptr=ptr->next;
		}
		printf("NULL");
	}
	//For Inserting a Node at the End of the List
	else if(ch==3){
		ctr = getNode();
		printf("Enter the Data for the Node :");
		scanf("%d",&ctr->data);
		while(ptr!=NULL){
			if(ptr->next==NULL){
				ptr->next=ctr;
				ctr->next=NULL;
			}
			ptr=ptr->next;
		}
		ptr=first;
		puts("Linked List Now :");
		while(ptr!=NULL){
			printf("%d => ",ptr->data);
			ptr=ptr->next;
		}
		printf("NULL");
	}
	//For Deleting a Node at the Beginning of the List
	else if(ch==4){
		first=ptr->next;
		ptr->next=NULL;
		free(ptr);
		ptr=first;
		puts("Linked List Now :");
		while(ptr!=NULL){
			printf("%d => ",ptr->data);
			ptr=ptr->next;
		}
		printf("NULL");
	}
	//For Deleting a Node at Kth Position  of the List
	else if(ch==5){
		puts("Enter the Position :");
		scanf("%d",&pos);
		int c=0;
		while(ptr!=NULL){
			c++;
			if(c==(pos-1)){
				node *nex;
				nex=ptr->next;
				ptr->next=nex->next;
				free(nex);
			}
			ptr=ptr->next;
		}
		ptr=first;
		puts("Linked List Now :");
		while(ptr!=NULL){
			printf("%d => ",ptr->data);
			ptr=ptr->next;
		}
		printf("NULL");
	}
	//for Deleting a Node at the End of the List
	else if(ch==6){
		while(ptr!=NULL){
			if(ptr->next->next==NULL){
				node *nex;
				nex=ptr->next;
				ptr->next=NULL;
				free(nex);
				break;
			}
			ptr=ptr->next;
		}
		ptr=first;
		puts("Linked List Now :");
		while(ptr!=NULL){
			printf("%d => ",ptr->data);
			ptr=ptr->next;
		}
		printf("NULL");
	}
}
