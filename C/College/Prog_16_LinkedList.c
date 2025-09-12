#include<stdio.h>
#include<stdlib.h>

struct Node{
   int data;
   struct Node* next;
};

int main(){
   struct Node *start,*current, *previous;
   int n,x;
   printf("Enter no of Nodes to be created:");
   scanf("%d",&n);

   printf("Enter Data for Node 1:");
   scanf("%d",&x);

   start= (struct Node*)malloc(sizeof(struct Node));
   start->data=x;
   start->next=NULL;
   previous=start;
   for (int i = 1; i < n; i++)
   {
      printf("Enter Data for Node %d:",i+1);
      scanf("%d",&x);
      
      current= (struct Node*)malloc(sizeof(struct Node));
      current->data=x;
      current->next=NULL;
      previous->next=current;
      previous=current;
   }

   printf("Linked List\n");
   current=start;
   while(current->next !=NULL){
      printf("%d -> ",current->data);
      current=current->next;
   }
   printf("%d ->",current->data);
   printf("NULL\n");
   

   return 0;
}