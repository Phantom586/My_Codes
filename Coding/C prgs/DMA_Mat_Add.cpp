#include<stdio.h>
#include<malloc.h>
#include<string.h>
#include<stdlib.h>
main(){
	int *mat1,*mat2,*mat3;
	int i,j,m,n,p,q;
	puts("Enter the Dimensions of the First Array :");
	scanf("%d %d",&m,&n);
	puts("Enter the Dimensions of the Second Array :");
	scanf("%d %d",&p,&q);
	if(n!=p){
		puts("Dimensions not Correct :");
		exit(1);
	}
	else{
		mat1=(int*)malloc(m*n*sizeof(int));
		mat2=(int*)malloc(m*n*sizeof(int));
		mat3=(int*)malloc(m*n*sizeof(int));
		if(mat1==NULL || mat2==NULL || mat3==NULL){
			puts("Problem Occurred !!");
			exit(1);
		}
		else{
			printf("Enter the %d Elements of the First Matrix :",m*n);
			for(i=0;i<m;i++){
				for(j=0;j<n;j++){
					scanf("%d",&mat1[i*n+j]);
				}
			}
			printf("Enter the %d Elements of the Second Matrix :",p*q);
			for(i=0;i<p;i++){
				for(j=0;j<q;j++){
					scanf("%d",&mat2[i*n+j]);
				}
			}
			puts("The Addition of the Two Matrix :");
			for(i=0;i<m;i++){
				for(j=0;j<n;j++){
					mat3[i*n+j]= mat1[i*n+j]+mat2[i*n+j];
				}
			}
			
			for(i=0;i<m;i++){
				for(j=0;j<n;j++){
					printf("%d ",mat3[i*n+j]);
				}
			}
		}
	}
}
