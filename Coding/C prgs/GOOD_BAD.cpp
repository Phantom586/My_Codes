#include <stdio.h>
int main()
{
	int len;
	scanf("%d",&len);
		int length, E, Cap=0, Small=0, i;
		char S;
    for (int j = 0; j <len; j++)
	{
		scanf("%d ",&length);
		scanf("%d\n",&E);
		
		for (i=1; i<=length;i++)
		{
			scanf("%c",&S);
			if (S<='Z' && S>='A')
				{
					Cap++;
				}
			if(S <= 'z' && S >= 'a') 
			{
					Small++;
 
			} 
		}
 
    		if(Small <= E && Cap <= E)
			{
				printf("both\n");
			}
			else if (Small<=E)
			{
				printf("brother\n");
			}
			else if (Cap<=E)
			{
				printf("chef\n");
			}
			else
				printf("none\n");
			
			Cap=0;
			Small=0;
 
	}	
 
return 0;
}
