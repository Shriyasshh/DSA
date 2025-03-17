# Selection Sort
# The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.

# To implement the Selection Sort algorithm in a programming language, we need:

# 1. An array with values to sort.
# 2. An inner loop that goes through the array, finds the lowest value, and moves it to the front of the array. 
#   This loop must loop through one less value each time it runs.
# 3. An outer loop that controls how many times the inner loop must run. For an array with 
#  n values, this outer loop must run  n − 1 times.


# my_array = [64, 34, 25, 5, 22, 11, 90, 12]

# n = len(my_array)
# for i in range(n-1):
#     min_index = i
#     print("min_index:", min_index)
#     for j in range(i+1, n):
#         if my_array[j] < my_array[min_index]:
#             min_index = j
#     min_value = my_array.pop(min_index)
#     print("min_value:", min_value)
#     my_array.insert(i, min_value)

# print("Sorted array:", my_array)


# Shifting Problem

# In the code above, the lowest value element is removed, and then inserted in front of the array.

# Each time the next lowest value array element is removed, 
# all following elements must be shifted one place down to make up for the removal.


# Solution
# Instead of all the shifting, swap the lowest value  with the first value .

my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)
for i in range(n):   #or #(n-1)
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i],my_array[min_index]=my_array[min_index],my_array[i]
    print("Sorted array:", my_array)


# Selection Sort sorts an array of n values.

# On average, about n/2 elements are compared to find the lowest value in each loop.
# And Selection Sort must run the loop to find the lowest value approximately n times.

# We get time complexity: O(n/2⋅n)=O(n^2)


# The most significant difference from Bubble sort that we can notice in this simulation is 
# that best and worst case is actually almost the same for 
# Selection Sort (O(n2)), 
# but for 
# Bubble Sort the best case runtime is only O(n).