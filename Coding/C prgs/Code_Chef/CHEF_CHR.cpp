#include<stdio.h>
#include<string.h>
main(){
	int t,i,j;
	int c,c1;
	char str[100];
	scanf("%d",&t);
	fflush(stdin);
	while(t--){
		gets(str);
		c1=0;
		for(i=0;str[i]!='\0';i++){
			c=0;
			for(j=i;j<(i+4);j++){
				if(str[j]=='c' || str[j]=='h' || str[j]=='e' || str[j]=='f'){
					c++;	
				}				
			}
		if(c==4)
		c1++;	
		}
		if(c1!=0)
		printf("lovely %d",c1);
		else
		printf("normal");
	}
}
