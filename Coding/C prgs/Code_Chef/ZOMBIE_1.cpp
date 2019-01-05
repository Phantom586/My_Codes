#include<stdio.h>
main(){
	int t;
	scanf("%d",&t);
	while(t--){
		int N,M,i,j,a;
		scanf("%d %d",&N,&M);
		int Z[N],CR[M][3];
		//int max[M],max_arr[M];
		for(i=0;i<N;i++)
		scanf("%d",&Z[i]);
		for(i=0;i<M;i++){
			for(j=0;j<3;j++){
				scanf("%d",&CR[i][j]);
			}
		}
		/*printf("\n");
		for(i=0;i<M;i++){
			for(j=0;j<3;j++){
				
				printf("%d ",CR[i][j]);
			}
			printf("\n");
		}
		for(i=0;i<M;i++){
				max[i]=CR[i][1]-CR[i][0];
				max_arr[i]=CR[i][1]-CR[i][0];
			}
		//Sorting the Array	
		for (i = 0; i < M; ++i) 
        {
            for (j = i + 1; j < M; ++j) 
            {
                if (max[i] < max[j]) 
                {
                    a = max[i];
                    max[i] = max[j];
                    max[j] = a;
                }
            }
        }
        for(i=0;i<M;i++){
        	for(j=0;j<M;j++){
        		if(max[i]==max_arr[j]){
        			pos[i]=j;
        			if(max[i]==max[i+1])
        			break;
				}
			}
		}*/
		x:
			int c=0,d=0,L=0,R=0,k,pos[M]={0};
			int s=1;
		for(i=0;i<M;i++){
			if(Z[i]>0){
				pos[i]=i+1;
			}
			else{
				Z[i]=0;
				d++;
			}
			//while(s<CR[L][2])
				//Z[i]-=s;
		}
		L=pos[d];
		R=pos[(i-1)];
		for(i=0;i<M;i++){
			if(CR[i][0]==L && CR[i][1]==R){
				printf("Position : CR[%d][%d]\n",i,i);
				k=CR[i][2];
				for(j=(L-1);j<=(R-1);j++){
					Z[j]-=s;
				}
				CR[i][2]--;
				}
			else{
				int a,b,c,d;
				a=L+1;b=R+1;c=L-1;d=R-1;
				if(d<=i){
					if(CR[i][0]==L && CR[i][1]==d){
					L--;
					}
				}
				
			}
		}
		for(i=0;i<M;i++){
			if(Z[i]>0)
			c++;
		}
		if(c!=0)
		goto x;
		for(i=0;i<M;i++)
		printf("%d ",Z[i]);
	}
}
