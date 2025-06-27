# Linear Search
# The Linear Search algorithm searches through an array and 
# returns the index of the value it searches for.

# How it works:

# 1.Go through the array value by value from the start.
# 2.Compare each value to check if it is equal to the value we are looking for.
# 3.If the value is found, return the index of that value.
# 4.If the end of the array is reached and the value is not found, 
#   return -1 to indicate that the value was not found.

# Linear Search Implementation
# To implement the Linear Search algorithm we need:

# 1.An array with values to search through.
# 2.A target value to search for.
# 3.A loop that goes through the array from start to end.
# 4.An if-statement that compares the current value with the target value, and returns the current index if the target value is found.
# 5.After the loop, return -1, because at this point we know the target value has not been found.

def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

arr = [3, 7, 2, 9, 5]
targetVal = 9

result = linearSearch(arr, targetVal)

if result != -1:
    print("Value",targetVal,"found at index",result)
else:
    print("Value",targetVal,"not found")

# Linear Search Time Complexity

# If Linear Search runs and finds the target value as the first array value in an array with 
# n values, only one compare is needed.

# But if Linear Search runs through the whole array of n 
# values, without finding the target value, n compares are needed.

# This means that time complexity for Linear Search is:
# O(n)