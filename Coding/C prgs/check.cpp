#include<stdio.h>
main()
{
	char a[] = {1,2,3,4};
	char *ptr1 = a;
	char *ptr2 = a+3;
	printf("%d %d",ptr1,ptr2);
}
