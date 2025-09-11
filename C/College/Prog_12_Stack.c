#include <stdio.h>

int main()
{
   int stk[10], top = -1, n, elem, c = -1, fun;
   printf("Enter number limit:");
   scanf("%d", &n);

   while (c == -1)
   {
      printf("\n1-Push\n2-Pop\n3-Display\n4-Quit\nEnter:");
      scanf("%d", &fun);
      if (fun == 1)
      {
         printf("\nEnter Element:");
         scanf("%d", &elem);
      }

      switch (fun)
      {
      case 1:
         // printf("top");
         if (top == n - 1)
         {
            printf("\nStack is Full");
         }
         else
         {
            top++;
            stk[top] = elem;
         }
         break;
      case 2:
         if (top == -1)
         {
            printf("\nStack is Empty");
         }
         else
         {
            printf("\nElement %d is removed", stk[top]);
            top--;
         }
         break;
      case 3:
         if (top == -1)
         {
            printf("Stack is Empty");
         }
         else
         {
            for (int i = top; i >= 0; i--)
            {
               printf("%d ", stk[i]);
            }
         }
         printf("\n\n");
         break;

      case 4:
         c++;
         break;
      default:
         printf("\nInvalid Input");
         break;
      }
   }

   return 0;
}