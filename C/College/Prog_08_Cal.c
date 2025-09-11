#include <stdio.h>

int add(int x ,int y){
   int z;
   z=x+y;
   return z;
}

int sub(int x ,int y){
   int z;
   z=x-y;
   return z;
}
int pro(int x ,int y){
   int z;
   z=x*y;
   return z;
}
float div(int x ,int y){
   int z;
   z=(float) x/y;
   return z;
}

int main(){

   int C,n1,n2,out1;
   float out2;
   printf("1 -Addition\n");
   printf("2 -Subtraction\n");
   printf("3 -Multiplication\n");
   printf("4 -Division\n");
   printf("Enter which calculation to be performed: ");
   scanf("%d",&C);

   printf("Enter the nos: ");
   scanf("%d",&n1);
   scanf("%d",&n2);

   switch (C)
   {
   case 1:
      out1=add(n1,n2);
      printf("%d",out1);
      break;
   
   case 2:
      out1=sub(n1,n2);
      printf("%d",out1);
      break;
   
   case 3:
      out1=pro(n1,n2);
      printf("%d",out1);
      break;
   
   case 4:
      out2=div(n1,n2);
      printf("%.2f",out2);
      break;
   
   default:
      printf("Invalid Input");
      break;
   }


return 0;

}