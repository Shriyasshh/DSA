#include<stdio.h>

int main(){

   int arr1[5]={2,4,5,8,10};
   int arr2[6]={1,3,6,17,19,20};
   
   int m = sizeof(arr1)/sizeof(arr1[0]);
   int n = sizeof(arr2)/sizeof(arr2[0]);
   
   int size = m + n;

   // printf("%d\n", size);

   int arr3[(int)size];
   
   int i = 0;
   int j = 0;
   int k = 0;

   while( i != m && j != n  ){
      if(arr1[i] > arr2[j]){
         arr3[k] = arr2[j];
         j++;
         k++;
      }
      else if(arr1[i] < arr2[j]){
         arr3[k] = arr1[i];
         k++;
         i++;
      }
      
   }

  while(i != m)
  {
         arr3[k] = arr1[i];
         i++;
         k++;
   }
   
   while(j != n)
   {
         arr3[k] = arr2[j];
         j++;
         k++;
   }
   

   for(int i=0;i< size ;i++){
         printf("\n%d ",arr3[i]);  

   }
   return 0;
}