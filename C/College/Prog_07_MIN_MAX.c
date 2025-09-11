#include<stdio.h>

int main(){

   int arr[6]={2,9,5,8,7,10};
   int n=sizeof(arr)/sizeof(arr[0]);

   int largest=0,smallest=100;

   for (int i=0;i<n;i++)
   {
      if (arr[i]>largest){
         largest=arr[i];
      }
      if (arr[i]<smallest){
         smallest=arr[i];
      }
   }
   printf("Largest %d \n", largest);
   printf("Smallest %d", smallest);

   return 0;
}