# Binary Search
# The Binary Search algorithm searches through an array and 
# returns the index of the value it searches for.

# How it works:

# 1.Check the value in the center of the array.
# 2.If the target value is lower, search the left half of the array. 
#   If the target value is higher, search the right half.
# 3.Continue step 1 and 2 for the new reduced part of the array until 
#   the target value is found or until the search area is empty.
# 4.If the value is found, return the target value index. 
#   If the target value is not found, return -1.

# Binary Search Implementation
# To implement the Binary Search algorithm we need:

# 1.An array with values to search through.
# 2.A target value to search for.
# 3.A loop that runs as long as left index is less than, 
#   or equal to, the right index.
# 4.An if-statement that compares the middle value with the target value, 
#   and returns the index if the target value is found.
# 5.An if-statement that checks if the target value is less than, or larger than, 
#   the middle value, and updates the "left" or "right" variables to narrow down the search area.
# 6.After the loop, return -1, because at this point we know the target value has not been found.

def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid
        
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15

result = binarySearch(myArray, myTarget)

if result != -1:
    print("Value",myTarget,"found at index", result)
else:
    print("Target not found in array.")

# Binary Search Time Complexity

# Each time Binary Search checks a new value to see if it is the target value, 
# the search area is halved.

# This means that even in the worst case scenario where Binary Search cannot 
# find the target value, it still only needs log2n comparisons to look through a 
# sorted array of n values.

# Time complexity for Binary Search is:
# O(log2n)
