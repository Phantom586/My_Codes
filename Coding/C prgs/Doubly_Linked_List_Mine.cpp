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
			ctr=last=ptr;
		}
		puts("\nContinue : Y or N");
		choice = getch();
	}while(choice == 'Y'|| choice=='y');
	ptr=head;
	if(count > 0){
		printf("\n\nTraversing Doubly Linked List in Forward Direction :");
		while(ptr!=NULL){
			printf("%d <=> ",ptr->data);
			ptr=ptr->next;
		}
		printf("NULL");
		printf("\n\nTraversing Doubly Linked List in Backward Direction :");
		while(ctr!=NULL){
			printf("%d <=> ",ctr->data);
			ctr=ctr->prev;
		}
		printf("NULL");
	}
	ptr=head;
	printf("\n\n\nSelect Operation to be Performed :");
	printf("\n\nPress 1 for Inserting a Node at the Beginning of the List :");
	printf("\nPress 2 for Inserting a Node after Kth position in the List :");
	printf("\nPress 3 for Inserting a Node at the End of the List :");
	printf("\n");
	printf("\nPress 4 for Deleting a Node at the Beginning of the List :");
	printf("\nPress 5 for Deleting a Node at Kth Position  of the List :");
	printf("\nPress 6 for Deleting a Node at the End of the List :");
	scanf("%d",&ch);
	//For Inserting a Node at the Beginning of the List
	if(ch==1){
		ctr=getNode();
		printf("Enter the Data for the Node :");
		scanf("%d",&ctr->data);
		ctr->next=head;
		head->prev=ctr;
		ctr->prev=NULL;
		head=ctr;
		puts("Doubly Linked List Now :");
		while(ctr!=NULL){
			printf("%d <=> ",ctr->data);
			ctr=ctr->next;
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
				ctr->prev=ptr;
				ptr->next=ctr;
				ptr=ctr->next;
				ptr->prev=ctr;
				break;
			}
			ptr=ptr->next;
		}
		ptr=head;
		puts("");
		puts("Doubly Linked List Now :");
		while(ptr!=NULL){
			printf("%d <=> ",ptr->data);
			ptr=ptr->next;
		}
		printf("NULL");
	}
	//For Inserting a Node at the End of the List
	else if(ch==3){
		ctr = getNode();
		printf("Enter the Data for the Node :");
		scanf("%d",&ctr->data);
		ctr->prev=last;
		last->next=ctr;
		ctr->next=NULL;
		last=ctr;
		puts("");
		puts("Doubly Linked List Now :");
		while(ptr!=NULL){
			printf("%d <=> ",ptr->data);
			ptr=ptr->next;
		}
		printf("NULL");
	}
	//For Deleting a Node at the Beginning of the List
	else if(ch==4){
		head=ptr->next;
		head->prev=NULL;
		free(ptr);
		ptr=head;
		puts("Doubly Linked List Now :");
		while(ptr!=NULL){
			printf("%d <=> ",ptr->data);
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
				node *nex,*nnex;
				nex=ptr->next;
				ptr->next=nex->next;
				nnex=nex->next;
				nnex->prev=ptr;
				free(nex);
				break;
			}
			ptr=ptr->next;
		}
		ptr=head;
		puts("");
		puts("Doubly Linked List Now :");
		while(ptr!=NULL){
			printf("%d <=> ",ptr->data);
			ptr=ptr->next;
		}
		printf("NULL");
	}
	//For Deleting a Node at the End of the List
	else if(ch==6){
		node *nex;
		nex=last->prev;
		nex->next=NULL;
		free(last);
		last=nex;
		puts("");
		puts("Doubly Linked List Now :");
		while(ptr!=NULL){
			printf("%d <=> ",ptr->data);
			ptr=ptr->next;
		}
		printf("NULL");
	}
}
