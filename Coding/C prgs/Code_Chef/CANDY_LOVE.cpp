#include<stdio.h>
#include<string.h>
main(){
	int t;
	scanf("%d",&t);
	while(t--){
		int N;
		scanf("%d",&N);
		int i,A[N],a,b,c;
		for(i=0;i<N;i++)
		scanf("%d",&A[i]);
		for(i=0;i<N;i++){
			if(A[i]>A[i+1]){
				if((A[i]-A[i+1])==1){
					puts("Yes");
				}
				else{
					A[i]--;
					A[i+1]++;
				}
			}
			
		}
	}
}
