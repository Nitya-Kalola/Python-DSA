# Factorial of Number
def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1) # Functional Recursion - Includes Flow (num-1) and Base case (num==0 or num==1).

print(factorial(5))

# Time Complexity - O(N)
# Space Complexity - O(N) - Stack Space