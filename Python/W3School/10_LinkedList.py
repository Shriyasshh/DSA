# Linked List

# W3Schools DSA Linked List 
# https://www.w3schools.com/dsa/dsa_theory_linkedlists.php

# Practically useful

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:   # if list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # move to the last node
            current = current.next
        current.next = new_node

    # Print the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("null")


# Example usage:
ll = LinkedList()
values = [3, 5, 13, 2]

for v in values:
    ll.append(v)

ll.display()


# or
# Helpful for learning

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")

