def Fibonacci_Series(num):
    if num == 0 or num == 1:
        return num
    return Fibonacci_Series(num-1)+Fibonacci_Series(num-2)

print(Fibonacci_Series(5))

# Time Complexity - O(2^N)
# Stack Complexity - O(2^N) - Stack Space