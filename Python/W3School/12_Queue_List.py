# Queues

# A queue is a collection of items that follows the FIFO (First In First Out) principle.
# The item that is added first to the queue will be the first one to be removed.

# Basic operations we can do on a queue are:

# Enqueue: Adds a new element to the queue.
# Dequeue: Removes and returns the first (front) element from the queue.
# Peek: Returns the first element in the queue.
# isEmpty: Checks if the queue is empty.
# Size: Finds the number of elements in the queue.

# Queue Implementation using Arrays

# Reasons to implement queues using arrays:
# Memory Efficient: Array elements do not hold the next elements address like linked list nodes do.
# Easier to implement and understand: Using arrays to implement queues require less code than using linked lists, and for this reason it is typically easier to understand as well.

# Reasons for not using arrays to implement queues:
# Fixed size: An array occupies a fixed part of the memory. This means that it could take up more memory than needed, or if the array fills up, it cannot hold more elements. And resizing an array can be costly.
# Shifting cost: Dequeue causes the first element in a queue to be removed, and the other elements must be shifted to take the removed elements' place. This is inefficient and can cause problems, especially if the queue is long.
# Alternatives: Some programming languages have built-in data structures optimized for queue operations that are better than using arrays.

queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

# Dequeue
element = queue.pop(0)
print("Dequeue: ", element)

# Peek
frontElement = queue[0]
print("Peek: ", frontElement)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))

# But to explicitly create a data structure for queues, with basic operations, we should create a queue class instead.

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", myQueue.queue)

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())