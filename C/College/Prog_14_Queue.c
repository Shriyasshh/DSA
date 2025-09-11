#include <stdio.h>
#define n 3
int queue[n];
int r, f;

void enqueue();
int dequeue();
void display();

int main()
{
    r = -1, f = -1;
    int c = 0, op, out;
    while (c == 0)
    {
        printf("\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\nEnter:");
        scanf("%d", &op);

        switch (op)
        {
        case 1:
            enqueue();
            break;
        case 2:
            out = dequeue();
            if(out != -1){
                printf("Dequeued element: %d\n", out);
            }
            else{
                printf("Queue is Empty");
            }
            break;
        case 3:
            display();
            break;
        case 4:
            c = 1;
            break;
        default:
            printf("Invalid option\n");
            break;
        }
    }
    return 0;
}

void enqueue()
{
    if (r == n - 1)
    {
        printf("Queue is Full\n");
    }
    else{
        int elem;
        printf("Enter Element:");
        scanf("%d",&elem);
        queue[++r]=elem;
    }
}

int dequeue(){
    if (f==r){
        return -1;
    }
    else{
        int x;
        x=queue[++f];
        return x;
    }
}

void display()
{
    if (f == r)
    {
        printf("Queue is Empty\n");
    }
    else
    {
        for (int i = f + 1; i <= r; i++)
        {
            printf("%d ", queue[i]);
        }
        printf("\n");
    }
}