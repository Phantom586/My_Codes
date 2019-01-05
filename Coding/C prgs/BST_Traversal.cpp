#include<stdio.h>
#include<stdlib.h>
typedef struct Node{
	int data;
	struct Node *left,*right;
}node;
	node *root = NULL;
node* getNode(int val){
	node *ptr = (node*)malloc(sizeof(node));
	ptr->data = val;
	ptr->left = NULL;
	ptr->right = NULL;
	return ptr;
}

void Preorder(node *root1){
	node *ptr;
	ptr = root1;
	if(ptr != NULL){
		printf("%d ",ptr->data);
		Preorder(ptr->left);
		Preorder(ptr->right);
		return;
	}
	else{
		return;
	}
}

node* BST_Insert(int data){
	node *p,*q,*ptr;
	ptr = getNode(data);
	if(root == NULL){
		root = ptr;
	}
	else{
		p = root;
		while(p != NULL){
			if(data < p->data){
				p = p->left;
			}
			else if(data > p->data){
				p = p->right;
			}
		}
		if(data < p->data)
			p = ptr;
		else if(data > p->data)
			p = ptr;
	}
	printf("%d\n",root);
}
int main(){
	char ch;
	int data,ch1;

	do{
		printf("\nEnter the Data :");
		scanf("%d",&data);
		BST_Insert(data);
		printf("%d",root);
		printf("\nDo you want to Continue : Y or N");
		fflush(stdin);
		ch = getchar();
	}while(ch == 'y' || ch == 'Y');
	printf("\n\npress 1 for Pre-Order Traversal :");
	printf("\npress 2 for In-Order Traversal :");
	printf("\npress 3 for Post-Order Traversal :");
	scanf("%d",&ch1);
	if(ch1 == 1){
		printf("\nThe PreOrder Traversal is :");
		Preorder(root);
	}
	else if(ch1 == 2){
		
	}
	else if(ch == 3){
		
	}
}
