#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int i,n,sum=0;
        scanf("%d",&n);
        int a[n];
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            sum=sum+a[i];
        }
        if(sum%2==0)
        {
            printf("NO\n");
 
        }
        else
        {
            printf("YES\n");
        }
    }
 
return 0;
}
