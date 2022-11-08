#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
   int i,a,b;

   char numToWords[11][12]= {"zero","one","two","three","four","five","six","seven","eight","nine","ten"};

    printf("Printing the location in the array:%s",numToWords[3]);
    // Print Strings 
    for (int i = 0; i < 11; i++)  
        printf("%s ",numToWords[i]);
   for(i=a;i<12;i++){
       
       printf("%s",numToWords[i]);
       if(a%2){
           printf("even");
       }else{
           printf("odd");
       }
       numToWords[i++];

   }
    return 0;
}
