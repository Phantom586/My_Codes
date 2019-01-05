#include <stdio.h>
 
int check_anagram(char [], char []);
 
int main()
{
   char str1[100], str2[100];
   int flag;
 
   printf("Enter first string\n");
   gets(str1);
 
   printf("Enter second string\n");
   gets(str2);
 
   flag = check_anagram(str1, str2);
 
   if (flag == 1)
      printf("\"%s\" and \"%s\" are anagrams.\n", str1, str2);
   else
      printf("\"%s\" and \"%s\" are not anagrams.\n", str1, str2);
 
   return 0;
}
 
int check_anagram(char str1[], char str2[])
{
   int first[26] = {0}, second[26] = {0}, c = 0;
 //
   while (str1[c] != '\0')
   {
      first[str1[c]-'a']++;
      c++;
   }
    c = 0;
    while (str2[c] != '\0')
   {
      second[str2[c]-'a']++;
      c++;
   }
 
   for (c = 0; c < 26; c++)
   {
      if (first[c] != second[c])
         return 0;
   }
 
   return 1;
}

