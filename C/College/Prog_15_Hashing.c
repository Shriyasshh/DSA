#include <stdio.h>
int arr[5];

// Inserting Element using Hashing and Probing
void hash()
{
   int elem, x, flag = 0;
   printf("\nEnter Element to be inserted:");
   scanf("%d", &elem);
   x = elem % 5;
   if (arr[x] == 0)
   {
      arr[x] = elem;
      flag = 1;
   }

   else
   {
      for (int i = 1; i < 5; i++)
      {
         x = (x + 1) % 5;
         if (arr[x] == 0)
         {
            arr[x] = elem;
            flag = 1;
            break;
         }
      }

      if (flag == 0)
      {
         printf("\nElement not Inserted. Array is Full.");
      }
   }
}
// Linear Search
int search()
{
   int no;
   printf("\nEnter number to Search for:");
   scanf("%d", &no);
   for (int i = 0; i < 5; i++)
   {
      if (arr[i] == no)
      {
         return 1;
      }
   }
   return 0;
}

int hashsearch()
{
   int no, r;
   printf("\nEnter number to Search for:");
   scanf("%d", &no);
   r = no % 5;
   if (arr[r] == no)
   {
      return 1;
   }
   else
   {
      for (int i = 1; i < 5; i++)
      {
         r = (r + 1) % 5;
         if (arr[r] == no)
         {
            return 1;
         }
      }
      return 0;
   }
}

   int main()
   {
      int oper, con = 1, op;
      while (con == 1)
      {
         printf("\n\n1-Insert Element\n2-Search Element\n3-Hash Search Element\n4-Quit\nEnter:");
         scanf("%d", &oper);

         switch (oper)
         {
         case 1:
            hash();
            break;

         case 2:
            op = search();
            if (op == 1)
            {
               printf("\nElement is Present in Array.");
            }
            else
            {
               printf("\nElement is Not Present");
            }
            break;
         case 3:
            op = hashsearch();
            if (op == 1)
            {
               printf("\nElement is Present in Array.");
            }
            else
            {
               printf("\nElement is Not Present");
            }
            break;
         case 4:
            con = 0;
            break;
         case 5:
            for (int i = 0; i < 5; i++)
            {
               printf("%d:%d\n", i, arr[i]);
            }
            break;
         default:
            printf("Invalid Input");
            break;
         }
      }

      return 0;
   }