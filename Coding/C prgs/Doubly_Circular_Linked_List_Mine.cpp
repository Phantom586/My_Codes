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
	char choice,c2;
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
	ptr=head;
	do{
		printf("\nSelect an Operation to be Performed :");
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
			printf("\nEnter the Data for the Node :");
			scanf("%d",&ctr->data);
			ptr->prev=ctr;
			ctr->next=ptr;
			ctr->prev=NULL;
			head=ctr;
			last->next=ctr;
			puts("Circular Linked List Now :");
			while(ptr!=ctr){
				printf("%d <=> ",ptr->data);
				ptr=ptr->next;
			}
			printf("%d",ptr->data);
		}
		//For Inserting a Node after Kth position in the List
		else if(ch==2){
			ptr=head->next;
			node *nex;
			puts("Enter the Position :");
			scanf("%d",&pos);
			int c=0;
			while(ptr!=head){
				c++;
				if(c==(pos-1)){
					ctr=getNode();
					printf("Enter the Data for the Node :");
					scanf("%d",&ctr->data);
					nex=ptr->next;
					ptr->next=ctr;
					ctr->prev=ptr;
					ctr->next=nex;
					nex->prev=ctr;
					break;
				}
				ptr=ptr->next;
			}
			ptr=head->next;
			puts("");
			puts("Circular Linked List Now :");
			while(ptr!=head){
				printf("%d <=> ",ptr->data);
				ptr=ptr->next;
			}
			printf("%d",ptr->data);
		}
		//For Inserting a Node at the End of the List
		else if(ch==3){
			ctr=getNode();
			printf("\nEnter the Data :");
			scanf("%d",&ctr->data);
			last->next=ctr;
			ctr->prev=last;
			ctr->next=head;
			last=ctr;
			ptr=head->next;
			puts("");
			printf("\nCircular Linked List Now :");
			while(ptr!=head){
				printf("%d <=> ",ptr->data);
				ptr=ptr->next;
			}
			printf("%d",ptr->data);
		}
		//For Deleting a Node at the Beginning of the List
		else if(ch==4){
			node *nex;
			nex=head->next;
			head=nex;
			last->next=head;
			free(ptr);
			ptr=head->next;
			puts("");
			printf("\nCircular Linked List Now :");
			while(ptr!=head){
				printf("%d <=> ",ptr->data);
				ptr=ptr->next;
			}
			printf("%d",ptr->data);
		}
		//For Deleting a Node at Kth Position  of the List
		else if(ch==5){
			ptr=head->next;
			node *nex,*prex;
			puts("Enter the Position :");
			scanf("%d",&pos);
			int c=1;
			while(ptr!=head){
				c++;
				if(c==(pos)){
					nex=ptr->next;
					prex=ptr->prev;
					prex->next=nex;
					nex->prev=prex;
					free(ptr);
					break;
				}
				ptr=ptr->next;
			}
			ptr=head->next;
			puts("");
			puts("Circular Linked List Now :");
			while(ptr!=head){
				printf("%d <=> ",ptr->data);
				ptr=ptr->next;
			}
			printf("%d",ptr->data);
		}
		//For Deleting a Node at the End of the List
		else if(ch==6){
			node *nex;
			nex=last->prev;
			nex->next=head;
			free(last);
			last=nex;
			ptr=head->next;
			puts("");
			puts("Circular Linked List Now :");
			while(ptr!=head){
				printf("%d <=> ",ptr->data);
				ptr=ptr->next;
			}
			printf("%d",ptr->data);
		}
		fflush(stdin);
		printf("\nWant to Continue : Y or N");
		c2=getch();
	}while(c2=='Y' || c2=='y');
}
