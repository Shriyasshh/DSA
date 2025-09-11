#include<stdio.h>

int main(){

   int arr[5]={2,5,6,4,8};
   
   int query;
   printf("Enter no to be found");
   scanf("%d",&query);
   int found=-1;

   for(int i=0; i<5;i++ )
   {
      if (arr[i]==query)
      {
         printf("Element found at pos %d",i+1);
         found=1;
         break;
      }
   }
   if (found==-1){
      printf("Element not found");
   }
   return 0;
}