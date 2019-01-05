#include<stdio.h>
#include<string.h>
main(){
	int t,N,minX,maxX,i,j,x,y,spam,nspam;
	scanf("%d",&t);
	while(t--){
		scanf("%d %d %d",&N,&minX,&maxX);
		int w[N],b[N];
		for(i=0;i<N;i++){
			scanf("%d %d",&w[i],&b[i]);
		}
		spam=0;
		nspam=0;
		for(i=minX;i<=maxX;i++){
			x=i;
			for(j=0;j<N;j++){
				y=(w[j]*x)+b[j];
				x=y;
			}
			if(y%2==0)
			nspam++;
			else
			spam++;
		}
	printf("%d %d",nspam,spam);
	}
}
