#include<stdio.h>

int main(){
   int m1,m2,m3,m4,m5;
   float avg,t;
   printf("Enter marks of five subjects: ");

   scanf("%d",&m1);
   scanf("%d",&m2);
   scanf("%d",&m3);
   scanf("%d",&m4);
   scanf("%d",&m5);

   t=(float)(m1+m2+m3+m4+m5);
   avg=t/5.0;
   printf("Marks in Sub1 %d \n",m1);
   printf("Marks in Sub2 %d \n",m2);
   printf("Marks in Sub3 %d \n",m3);
   printf("Marks in Sub4 %d \n",m4);
   printf("Marks in Sub5 %d \n",m5);
   printf("Average: %.2f",avg);
   return 0;
}