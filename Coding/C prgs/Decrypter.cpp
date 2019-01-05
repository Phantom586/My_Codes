#include<stdio.h>
#include<string.h>
#include<ctype.h>
main()
{
	char s[100],c;
	int i,j,n,step;
	puts("Decrypt your Message by Altering Steps in Alphabets :");
	puts("\nEnter a String to be Decrypted----->");
	gets(s);
	puts("Enter the Step Size :");
	scanf("%d",&step);
	n = strlen(s);
	for(i=0;i<n;i++){
		c=s[i];
		if(isupper(c)){
			if((c-step) >= 65){
				c-=step;
			}
			else{
				int rem = step-(c-65);
				c=(90-rem)+1;
			}
			printf("%c",c);
		}
		else if(islower(c)){
			if((c-step)>= 97){
				c-=step;
			}
			else{
				int rem = step-(c-97);
				c=(122-rem)+1;	
			}
			printf("%c",c);	
		}
		else if(c=='@'||c=='#'||c==' '||c=='$'||c=='-'){
			c-=step;
			printf("%c",c);
		}
	}
}
