#include<stdio.h>
#include<string.h>
main(){
	char str[100];
	int n,i,t;
	char temp;
	scanf("%d",&t);
	if(t>=1 && t<=1000){
		while(t--){
			scanf("%d",&n);
			fflush(stdin);
			if(n>=1 && n<=100)
			gets(str);
			if(n%2==0){
				for(int i=0;i<n;i+=2){
					temp=str[i];
					str[i]=str[i+1];
					str[i+1]=temp;
				}
			}
			else{
				char tmp=str[n-1];
				for(int i=0;i<n-1;i+=2){
					temp=str[i];
					str[i]=str[i+1];
					str[i+1]=temp;
				}
				str[n-1]=tmp;
			}
			for(i=0;i<n;i++){
				if(str[i]=='z')
				str[i]='a';
			}
			for(i=0;i<n;i++){
				int rem;
				char ch;
				ch=str[i];
				rem = (int)ch - 97;
				str[i]=(char)122-rem;
			}
			puts(str);
		}
	}
}
