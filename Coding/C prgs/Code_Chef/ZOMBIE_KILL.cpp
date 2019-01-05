#include<stdio.h>
main(){
	int t;
	scanf("%d",&t);
	while(t--){
		int N,M,i,j;
		scanf("%d %d",&N,&M);
		int Z[N],CR[M][3];
		for(i=0;i<N;i++)
		scanf("%d",&Z[i]);
		for(i=0;i<M;i++){
			for(j=0;j<3;j++){
				scanf("%d",&CR[i][j]);
			}
		}
		for(i=0;i<M;i++){
				printf("%d\n",CR[i][1]-CR[i][0]);
			}
		for(i=0;i<N;i++){
			if()
		}
	}
}
