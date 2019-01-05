#include<stdio.h>
#include<malloc.h>
#include<string.h>
typedef struct TRAIN{
	char name[20],starts[20],ends[20];
	struct TIME{int dh,dt,ah,at;}time;
	int pnr; 
}train;

main(){
	train *ptr,*first,temp;
	
	int n,i,j,h,m,count=0;
	puts("Enter the No. of Records :");
	scanf("%d",&n);
	ptr=(train*)calloc(n,sizeof(train));
	
	for(i=0;i<n;i++){
		puts("\nEnter the Train Number(PNR) :");
		scanf("%d",&(ptr+i)->pnr);
		fflush(stdin);
		puts("\nEnter Train Name :");
		gets((ptr+i)->name);
		puts("\nEnter the Start Station :");
		gets((ptr+i)->starts);
		puts("\nEnter the Destination Station :");
		gets((ptr+i)->ends);
		puts("\nEnter the Departure Time (hh:mm)");
		scanf("%d %d",&(ptr+i)->time.dh,&(ptr+i)->time.dt);
		puts("\nEnter the Arrival Time (hh:mm)");
		scanf("%d %d",&(ptr+i)->time.ah,&(ptr+i)->time.at);
	}
	for(i=0;i<n;i++){
		for(j=i+1;j<n;j++){
			if((ptr+i)->pnr > (ptr+j)->pnr){
				temp=*(ptr+j);
				*(ptr+j)=*(ptr+i);
				*(ptr+i)=temp;
			}
		}	
	}
	for(i=0;i<n;i++){
		puts("\n======================");
		puts("Train Details");
		puts("======================");
		printf("\nTrain : %d",i+1);
		printf("\nTrain Name :\t %s",(ptr+i)->name);
		printf("\nTrain Number :\t %d",(ptr+i)->pnr);
		printf("\nTrain Start Destination :\t %s",(ptr+i)->starts);
		printf("\nTrain Final Destination :\t %s",(ptr+i)->ends);
		printf("\nTrain Arrival Time :\t %d : %d",(ptr+i)->time.dh,(ptr+i)->time.dt);
		printf("\nTrain Departure Time :\t %d : %d",(ptr+i)->time.ah,(ptr+i)->time.at);
	}
	printf("\n\n");
	printf("Enter Arrival Search Time : (hh:mm)\n");
	scanf("%d%d",&h,&m);
	first=ptr;
	int cmp=0,cmp1=0;
	for(i=0;i<n;i++,ptr++)
	{
		cmp=(ptr+i)->time.ah;
		cmp1=(ptr+i)->time.at;
		if(cmp == h && cmp1 == m){
			puts("\n======================");
			puts("Trains are :");
			printf("Train : %d",i+1);
			printf("\nTrain Name :\t %s",ptr->name);
			printf("\nTrain Number :\t %d",ptr->pnr);
			printf("\nTrain Start Destination :\t %s",ptr->starts);
			printf("\nTrain Final Destination :\t %s",ptr->ends);
			count++;
		}
	
	}
	if(count==0)
	{
		puts("Not Found:");
	}
}
