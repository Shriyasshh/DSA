// Practically useful
#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* next;
};

int main() {
    struct node *start = NULL, *current, *previous;
    int n, i, x;

    printf("Enter number of nodes: ");
    scanf("%d", &n);

    // Create first node
    printf("Enter data for node 1: ");
    scanf("%d", &x);
    start = (struct node*) malloc(sizeof(struct node));
    start->data = x;
    start->next = NULL;
    previous = start;

    // Create remaining nodes
    for (i = 2; i <= n; i++) {
        printf("Enter data for node %d: ", i);
        scanf("%d", &x);

        current = (struct node*) malloc(sizeof(struct node));
        current->data = x;
        current->next = NULL;

        previous->next = current;  // link previous node to current
        previous = current;        // move previous forward
    }

    // Print the linked list
    printf("\nLinked List: ");
    current = start;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");

    return 0;
}

// Or
// Helpful for learning
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (!newNode) {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void printList(Node* node) {
    while (node) {
        printf("%d -> ", node->data);
        node = node->next;
    }
    printf("null\n");
}

int main() {
    Node* node1 = createNode(3);
    Node* node2 = createNode(5);
    Node* node3 = createNode(13);
    Node* node4 = createNode(2);

    node1->next = node2;
    node2->next = node3;
    node3->next = node4;

    printList(node1);

    // Free the memory
    free(node1);
    free(node2);
    free(node3);
    free(node4);

    return 0;
}