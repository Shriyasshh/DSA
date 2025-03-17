

# To implement the Bubble Sort algorithm in a programming language, we need:

# 1.An array with values to sort.
# 2.An inner loop that goes through the array and swaps values if the first value is higher than the next value. This loop must loop through one less value each time it runs.
# 3.An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
my_array = [4,7,2]
# Code 1:


# n = len(my_array)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if my_array[j] > my_array[j+1]:
#             my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

# print("Sorted array:", my_array)

# Code 2:
    #Improvised Bubble Sort 
    # Imagine that the array is almost sorted already

n = len(my_array)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
    if not swapped:
        break

print("Sorted array:", my_array)

