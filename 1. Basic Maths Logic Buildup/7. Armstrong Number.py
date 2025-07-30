# Armstrong Number

"""
Armstrong Number is the Number Which Looks Same as the Actual Number
When we Power each Digit of the Number with the Count of Digits in a Number and
add it with each other.

E.g. : 153

    It has the 3 Count of Digits... hence the equation becomes like
    1^3 + 5^3 + 3^3 => 1 + 125 + 27 => 153, which is same as the Actual Number.
"""
# Way 1:
def count_digits(num):
    if num == 0:
        return 1
    X = abs(num)
    count = 0
    while X != 0:
        X//=10
        count+=1
    return count

def Armstrong(num):
    X = num
    A = 0
    while X != 0:
        A += (X%10)**count_digits(num)
        X//=10
    return A == num

# Way 2:
def Armstrong1(num):
    X = num
    nod = len(str(num))
    total = 0
    while X != 0:
        total += (X%10)**nod
        X//=10
    return total == num

P = int(input("Enter No. : "))
print(Armstrong(P))
print(Armstrong1(P))
