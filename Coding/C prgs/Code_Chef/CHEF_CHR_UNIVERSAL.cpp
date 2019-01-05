#include<stdio.h>
#include<string.h>
int check(char str[],char s1[],int i,int l){
	int first[26] = {0}, second[26] = {0},c=0;
	
	while(str[c]!='\0')
   {
      first[str[c]-'a']++;
      c++;
   }
    c = 0;
    while (s1[c] != '\0')
   {
      second[s1[c]-'a']++;
      c++;
   }
 
   for (c = 0; c < 26; c++)
   {
      if (first[c] != second[c])
         return 0;
   }
 
   return 1;
}
main(){
	int t,i,j;
	int c,c1;
	char str[100],s1[100];
	scanf("%d",&t);
	fflush(stdin);
	while(t--){
		gets(str);
		gets(s1);
		int l=strlen(s1);
		char arr[20];
		c1=0;
		for(i=0;str[i]!='\0';i++){
			for(j=i;j<(i+l);j++){
				arr[j]=str[j];
					if(check(arr,s1,i,strlen(s1))==1)
					c1++;
			}
		}
		if(c1)
		printf("lovely %d",c1);
		else
		printf("normal");
	}
}
