 #include<stdio.h>

 void main()
 {
 int P1,P2,Q1,Q2,C1,C2,Sum;
 printf("Enter Cost of Item1:");
 scanf("%d",&P1);
 printf("Enter Quantity ofItem1:");
 scanf("%d",&Q1);
 printf("Enter Cost of Item2:");
 scanf("%d",&P2);
 printf("Enter Quantity of Item2:");
 scanf("%d",&Q2);
 Sum=(P1*Q1)+(P2*Q2);
 printf("Total is %d",Sum);
 }