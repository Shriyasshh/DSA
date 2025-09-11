# Study of Time Complexity
# time stamp 8:55:25


# Problem Find Sum of N natural numbers
# To cal time taken to run program we use time module


from time import time

# Soln 1

# def SumofN(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     return sum


# Soln 2

def SumofN(n):
    return int (n*(n+1))/2

# Program
st_time=time()
R=SumofN(1000000000000000)
end_time=time()
print(R)
print(end_time-st_time)