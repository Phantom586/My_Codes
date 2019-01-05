#include<stdio.h>
#include<stdlib.h>
#include<string.h>
main(){
	char arr[20],q[20];
	int t;
	scanf("%d",&t);
	while(t--){
		fflush(stdin);
		printf("\n");
		gets(arr);
		int c=0;
		for(int i=0;arr[i]!='\0';i++){
			if(arr[i] == '{' || arr[i] == '[' || arr[i] == '('){
				q[c] = arr[i];
				c++;	
			}
			else if(arr[i] == ')'){
				if(q[c-1] == '('){
					q[c-1] = '\0';
					c--;
				}
				else
					break;
			}
			else if(arr[i] == ']'){
				if(q[c-1] == '['){
					q[c-1] = '\0';
					c--;
				}
				else
					break;
			}
			else if(arr[i] == '}'){
				if(q[c-1] == '{'){
					q[c-1] = '\0';
					c--;
				}
				else
					break;
			}
		}
		if(c == 0)
			printf("Yes");
		else
			printf("No");	
	}
}
