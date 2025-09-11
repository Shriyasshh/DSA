#include<stdio.h>

int fact(int n){
   if (n==1){
      return 1;
   }
   
   return n*fact(n-1);
}

int main(){

   int n=5;
   int facto=fact(n);
   printf("Factorial of %d : %d",n, facto);

   return 0;
}