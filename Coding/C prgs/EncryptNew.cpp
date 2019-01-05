#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>
#include<time.h>
#include<stdlib.h>

main()
{
	int n,a,b,f1,f2,num[20];
	char k1[5],k2[5],str[100];
	puts("Asymmetric Encryption");
	puts("Bits Encryption :By Ph@ntom");
	puts("\nEnter the Code to be Encrypted");
	gets(str);
	n = strlen(str);
	/*srand(time(0));
	for(int i=0;i<2;i++){
		if(i==0){
		a = rand();
		continue;
		}
		b = rand();
		printf("Random Numbers : %d----%d",a,b);
	}*/
		
	/*for(int i=0;i<n;i++){
		int c = str[i];
		num[i]=int(c);
		printf("\nChar to int : %d",num[i]);
	}*/
		a = str[0];
		b = str[1];
		f1 = pow((a+b),2);
		f2 = (a*a + b*b + 2*a*b);
		printf("\nFormulae : %d and %d---",f1,f2);
		/*for(int i=0;i<f1.length();i++){
			
		}*/
		char j=char(f1);
		char k=char(f2);
		printf("\nChar to int : %c ----- %c",j,k);
}
