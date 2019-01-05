#include<stdio.h>
#include<string.h>
#include<ctype.h>
main()
{
	char s[100],c;
	int i,j,n,step;
	puts("Encrypt your Message by Altering Steps in Alphabets :");
	puts("\nEnter a String to be Encrypted----->");
	gets(s);
	puts("Enter the Step Size :");
	scanf("%d",&step);
	n = strlen(s);
	for(i=0;i<n;i++){
		c=s[i];
		if(isupper(c)){
			if((c+step) <= 90){
				c+=step;
			}
			else{
				int rem = step-(90-c);
				c=(65+rem)-1;	
			}
			printf("%c",c);
		}
		else if(islower(c)){
			if((c+step) <= 122){
				c+=step;
			}
			else{
				int rem = step-(122-c);
				c=(97+rem)-1;	
			}
			printf("%c",c);	
		}
		else if(c=='@'||c=='#'||c==' '||c=='$'||c=='-'){
			c+=step;
			printf("%c",c);
		}
	}
}
