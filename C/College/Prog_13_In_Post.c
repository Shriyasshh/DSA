#include <stdio.h>
#include <string.h>
#include <ctype.h>

// function prototype
char* intopost(char infix[]);

int prec(char c){
   if (c=='*' || c=='/'){
      return 2;
   }
   if (c=='+'|| c=='-'){
      return 1;
   }
   if (c=='(' || c==')'){
      return 0;
   }
   return -1;   // added return for other cases
}

int main()
{
   char infix[10];
   char* postfix;

   printf("Enter infix expression: ");
   scanf("%s", infix);   // removed &

   postfix = intopost(infix);
   printf("Postfix: %s",postfix);
   return 0;
}

char* intopost(char infix[])
{
   int top = -1,count = -1;
   char stk[10];
   int len= strlen(infix);
   char c;
   static char op[10];

   for (int i = 0; i < len; i++)
   {
      c = infix[i];
      int pre = prec(c);
      char ch;

      if (isalnum(c))
      {
         op[++count] = c;
      }
      else if (c == '(')
      {
         stk[++top] = c;
      }
      else if (c == ')')
      {
         while (top >= 0 && stk[top] != '(')
         {
            op[++count] = stk[top--];
         }
         if (top >= 0) top--;   // discard '('
      }
      else if (pre > 0)
      {
         while (top >= 0 && prec(stk[top]) >= pre)
         {
            op[++count] = stk[top--];
         }
         stk[++top] = c;
      }
   }
   while (top >= 0) {
        op[++count] = stk[top--];
    }

    op[++count] = '\0'; 
    return op;
}
