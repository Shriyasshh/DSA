#include<stdio.h>

struct Rec
{
   int r,c,val;
};

int main(){

   struct Rec M1[10];   
   {
      printf("Enter no of NON zero elements: ");
      scanf("%d",&M1[0].val);
      printf("%d\n",M1[0].val);

      printf("Enter no of rows and cols: ");
      scanf("%d %d",&M1[0].r,&M1[0].c);

      for (int i = 1; i <= M1[0].val; i++)
      {
         printf("Enter Row no,Col no, Value ");
         scanf("%d %d %d",&M1[i].r,&M1[i].c,&M1[i].val);
      }

      printf("\nRows Columns Value\n");
      for (int i = 0; i <= M1[0].val; i++)
      {
         printf(" %d    %d     %d\n",M1[i].r,M1[i].c,M1[i].val);
      }
   };
   
   return 0;
}
