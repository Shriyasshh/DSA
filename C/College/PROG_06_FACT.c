# include <stdio.h>

int main(){

   int no, fact=1;
   printf("Enter no to find factorial of: ");
   scanf("%d",&no);

   for (int i=1;i<=no;i++){
      fact*=i;
   }
   printf("Factorial of %d is %d",no,fact);
   return 0;
}