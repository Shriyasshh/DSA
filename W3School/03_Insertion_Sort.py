# Insertion Sort
# The Insertion Sort algorithm uses one part of the array to hold the sorted values,
# and the other part of the array to hold values that are not sorted yet.

# Insertion Sort Implementation
# 1.An array with values to sort.

# 2.An outer loop that picks a value to be sorted. For an array with n values, 
# this outer loop skips the first value, and must run n−1 times.

# 3.An inner loop that goes through the sorted part of the array, to find where to insert the value. 
#   If the value to be sorted is at index i, the sorted part of the array starts at index 0 and ends at index i−1.



# my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# n = len(my_array)
# for i in range(1,n):
#     print("i:", i)
#     insert_index = i
#     current_value = my_array.pop(i)
#     print("pop_value:", current_value)
#     for j in range(i-1, -1, -1):
#         print("j:", j)
#         if my_array[j] > current_value:
#             insert_index = j
#             print("insert_index:", insert_index)
#     my_array.insert(insert_index, current_value)
#     print( my_array)

# print("Sorted array:", my_array)


# Insertion Sort Improvement/Problem

# The problem with this way of programming it is that when removing a value from the array,
#  all elements above must be shifted one index place down.
#And when inserting the removed value into the array again, there are also many shift operations that must be done: 
# all following elements must shift one position up to make place for the inserted value: 


# Hidden memory shifts: You will not see these shifting operations happening in the code if you are using a high-level programming language such as Python or JavaScript, 
# but the shifting operations are still happening in the background. Such shifting operations require extra time for the computer to do, which can be a problem.

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1,n):
    insert_index = i
    current_value = my_array[i]
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]
            insert_index = j
        else:
            break
    my_array[insert_index] = current_value

print("Sorted array:", my_array)


# Insertion Sort Time Complexity
# Insertion Sort sorts an array of n values.

# On average, each value must be compared to about n/2 other values to find the correct place to insert it.

# Insertion Sort must run the loop to insert a value in its correct place approximately n times.
# We get time complexity for Insertion Sort:
# O(n/2⋅n)=O(n^2)