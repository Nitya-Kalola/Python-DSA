# No. is Palindrome or Not

"""
Palindrome Number is the Number which looks Exactly Same to the Actual Number
when we reverse that Number.
"""

"""
Concepts used here:
    "Extraction of Digit" -> From File No. 4
"""

# Own Logic:
def Count_Digit(num):
    if num == 0:
        return 1
    X = abs(num)
    count = 0
    while X != 0:
        X//=10
        count+=1
    return count

def Reverse(num):
    X = num
    Y = 10**(Count_Digit(num)-1)
    B = 0
    while X != 0:
        B = Y*(X%10) + B 
        X//=10
        Y//=10
    return B

def Palindrome(num):
    return num == Reverse(num) # Returns True If both are same otherwise False.

# Optimized Way:
def Reverse(num):
    rev = 0
    X = abs(num)
    while X != 0:
        rev = rev * 10 + X % 10
        X //= 10
    return rev

def Palindrome(num):
    return num == Reverse(num)

"""
Time Complexity of Both the Approaches will be O(log10(N)), where N is a Number.
But the 1st approach is still Slower becasue of Complex Math Operations(**).

Space Complexity of Both the Approaches will be O(1), where N is a Number.
"""

Number = int(input("Enter Your Number : "))
print(Palindrome(Number))
