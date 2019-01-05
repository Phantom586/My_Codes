#include<string.h>
#include<stdio.h>
main()
{
	char c[20];
	int regexItem = new Regex("^[a-zA-Z0-9 ]*$");
	puts("Enter any String");
	gets(c);

	if(regexItem.IsMatch(c)){
		printf("Special Characters found!");
	}
	else
	printf("Not Found!");

}
