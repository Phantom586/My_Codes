#include<stdio.h>
 
int main(){
	int T;scanf("%d",&T);
	while(T--){
		int A[30];
		int c=0;
		for(int i=0;i<30;i++)
		scanf("%d ",&A[i]);
		for(int i=0;i<30;i++){
			if(A[i]==1){
				c++;
				if(c==6)
				break;
			}
			else 
			c=0;
		}
		if(c==6)printf("#coderlifematters\n");
		else printf("#allcodersarefun\n");
	}
	return 0;
}   
