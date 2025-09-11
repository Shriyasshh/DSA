# Quicksort
# As the name suggests, Quicksort is one of the fastest sorting algorithms.

# How it works:

# 1.Choose a value in the array to be the pivot element.
# 2.Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
# 3.Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
# 4.Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.

# Quicksort Implementation
# To write a 'quickSort' method that splits the array into shorter and shorter sub-arrays we use recursion.
# This means that the 'quickSort' method must call itself with the new sub-arrays to the left and right of the pivot element.

# To implement the Quicksort algorithm in a programming language, we need:

# 1. An array with values to sort.
# 2. A quickSort method that calls itself (recursion) if the sub-array has a size larger than 1.
# 3. A partition method that receives a sub-array, moves values around, swaps the pivot element into the sub-array and 
#	returns the index where the next split in sub-arrays happens.


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)


# Quicksort Time Complexity
# The worst case scenario for Quicksort is O(n^2). This is when the pivot element is either the highest 
# or lowest value in every sub-array, which leads to a lot of recursive calls. With our implementation above, 
# this happens when the array is already sorted.

# But on average, the time complexity for Quicksort is actually just O(nlogn), 
# which is a lot better than for the previous sorting algorithms we have looked at. 
# That is why Quicksort is so popular.

# Below you can see the significant improvement in time complexity for Quicksort in an average scenario O(nlogn), 
# compared to the previous sorting algorithms Bubble, Selection and Insertion Sort with time complexity O(n^2)


# Code

# def partition(array, low, high):
# 	pivot = array[high]
# 	print("pivot:", pivot)
# 	i = low - 1
# 	print("i_1:", i)

# 	for j in range(low, high):
# 		if array[j] <= pivot:
# 			i += 1
# 			print("i_2:",i,"j:",j)
# 			array[i], array[j] = array[j], array[i]
# 			print("array_if:", array)
# 		print("array_for:", array)

# 	array[i+1], array[high] = array[high], array[i+1]
# 	print("\n array_else:", array)
# 	return i+1

# def quicksort(array, low=0, high=None):
#     if high is None:
#         high = len(array) - 1

#     if low < high:
#         pivot_index = partition(array, low, high)
#         print("pivot_index_1:", pivot_index)
#         quicksort(array, low, pivot_index-1)
#         quicksort(array, pivot_index+1, high)
#         print("pivot_index_2:", pivot_index)

# my_array = [64, 34, 25, 12, 22, 11, 90, 5]
# quicksort(my_array)
# print("Sorted array:", my_array)