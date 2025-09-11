#include<stdio.h>
#include<conio.h>
int main(){

float f,c;
// clrscr();
printf("Enter Temperature in F:");
scanf("%f",&f);

c=(5.0/9)*(f-32);
printf("Temperature in C: %f",c);
getch();
return 0;
}