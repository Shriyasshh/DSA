#include<stdio.h>

int main(){
int amt,std, amt_dist,amt_bal;
printf("Enter amount to be distributed");
scanf("%d ",&amt);
printf("Enter no of Students");
scanf("%d",&std);

printf("Balance Amount: %d",amt%std);

}