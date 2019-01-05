#include<stdio.h>
#include<conio.h>
void main()
{

int row,colu,rows;
printf("enter the no:");
scanf("%d",&rows);
for(row=1;row<=rows;row++)
{
for(colu=1;colu<=row;colu++){
printf("%d",row);
}
printf("\n");
}
}
