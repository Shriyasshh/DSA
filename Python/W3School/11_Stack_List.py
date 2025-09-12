# Stack
# A stack is a data structure that can hold many elements.
# A stack is like a collection of items where you can only add or remove the top item.
# This is called a Last In First Out (LIFO) data structure because the last item added to the stack is the first item that can be removed.

# Basic operations we can do on a stack are:

# Push: Adds a new element on the stack.
# Pop: Removes and returns the top element from the stack.
# Peek: Returns the top element on the stack.
# isEmpty: Checks if the stack is empty.
# Size: Finds the number of elements in the stack.

# It can be implemented by using arrays or linked lists.



# Stack Implementation using Arrays

# Reasons to implement stacks using arrays:
# Memory Efficient: Array elements do not hold the next elements address like linked list nodes do.
# Easier to implement and understand: Using arrays to implement stacks require less code than using linked lists, and for this reason it is typically easier to understand as well.

# A reason for not using arrays to implement stacks:
# Fixed size: An array occupies a fixed part of the memory. This means that it could take up more memory than needed, or if the array fills up, it cannot hold more elements.

stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

# Pop
element = stack.pop()
print("Pop: ", element)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))




# But to explicitly create a data structure for stacks, with basic operations, we should create a stack class instead. 

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

# Create a stack
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')
print("Stack: ", myStack.stack)

print("Pop: ", myStack.pop())

print("Peek: ", myStack.peek())

print("isEmpty: ", myStack.isEmpty())

print("Size: ", myStack.size())