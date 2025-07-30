# Count the No. of Digit from an Integer

"""
Concept used here :
    "Extraction of Digit" -> In File No. 4
"""
# Way 1 : Using While Loop
X = int(input("Enter the No. : "))
Y = X
i = 0

while Y!=0:
    Y//=10
    i+=1
print(f"No. of Digits in {X} is {i}")

"""
Here Time Complexity(TC) of Code will be O(log10(N)), where N is Given Number...
If Y//5 is given Then its TC will be O(log5(N)).

And Space Complexity is O(1) here.
"""

# Way 2: Using Logarithm

"""
How it Works :
    If Number has Length of 4 then its log of Number to the base 10 is 3 point something...
    So if we add 1 in Generated Output and return in integer format we get Count of Digit in Number.
    
"""

from math import *

def CountDigit(num):
    return int(log10(num)+1)

# Way 3: Handling 0 and Negative Values.
def CountDigit1(num):
    if num == 0: # Handles If Input is 0 or 00 or 000 or ...
        return 1
    X = abs(Y) # Converts Negative No. to Positive if Negative
    Count = 0
    while X != 0:
        X //= 10
        Count += 1
    return Count

# Way 4: Short One
def count_digits(n):
    if n == 0:
        return 1
    return len(str(abs(n))) # Converts -ve Number to Positive in any, then it Converted to the String & Calculates its length.

