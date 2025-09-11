#include<stdio.h>

int fibo(int n){
   int f1=0,f2=1,f3, i=3;

   while (i <= n)
   {
      f3=f1+f2;
      f1=f2;
      f2=f3;
      i++;
   
   }
   return f3;
   // or
   //  if (n == 1) return 0;        
   // if (n == 2) return 1;

   // return fibo(n-1)+fibo(n-2);

         
}

int main(){

   int n=8;
   int fib=fibo(n);
   printf("fibbonnaci series element at  %d : %d",n, fib);

   return 0;
}


















//  if (n == 1) return 0;        
   // if (n == 2) return 1;

   // return fibo(n-1)+fibo(n-2);