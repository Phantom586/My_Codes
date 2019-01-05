#include<stdio.h>
#include<string.h>
main(){
	int t,j=1;
	scanf("%d",&t);
	while(t--){
		char str[1000];
		int M,N,Rx,Ry,n;
		scanf("%d %d",&M,&N);
		scanf("%d %d",&Rx,&Ry);
		scanf("%d",&n);
		fflush(stdin);
		gets(str);
		int x=0,y=0;
		for(int i=0;str[i]!='\0';i++){
			if(str[i]=='L')
			x=x-1;
			else if(str[i]=='D')
			y=y-1;
			else if(str[i]=='U')
			y=y+1;
			else if(str[i]=='R')
			x=x+1;
		}
		if(x==Rx && y==Ry)
		printf("Case %d: Reached",j);
		else if(x>M || y>N)
		printf("Case %d: Dangerous",j);
		else
		printf("Case %d: Random",j);
		j++;
	}
	
}
