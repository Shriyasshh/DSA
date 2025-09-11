#include <stdio.h>

int fact(int x){
   int facto=1;
   // printf("%d",x);
   for (int i=1; i<=x;i++)
   {
      facto*=i;
   }
   return facto ;

};

int main(){
   int n=5, r=2 ;
   float  x,y,z,soln;
   x=fact(n);
   printf("x= %.f\n",x);

   y=fact(r);
   printf("y= %.f\n",y);

   z=fact(n-r);
   printf("z= %.f\n",z);

   soln=x/(y*z);
   printf("%.2f",soln);

   return 0;
   
}