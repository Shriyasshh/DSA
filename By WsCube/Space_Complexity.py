# Study of Space Complexity
# time stamp 9:04:41

# tracemalloc is used to track memory usage

# program

import tracemalloc as tm

# Soln 1

'''def SumofN(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
'''

# Soln 2

def SumofN(n):
    return int (n*(n+1))/2

# Program

tm.start()
R=SumofN(100)
print(R)

print(tm.get_traced_memory())
tm.stop()
