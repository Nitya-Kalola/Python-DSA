# Print all the Factors/Divisors of the Given Number

"""
"""

# Way 1 ->  Extream Brute Force(Worst Code)
num = int(input("Enter the Number : "))
X = num
List = []
i = 1

while i != X+1:
    if X%i == 0:
        List.append(i)
    i+=1

"""
TC of this is O(N) & SC is O(k), where k is the No. of Factors/Divisors.
"""

print(List)

# Way 2 -> Better Solutions
j = 1
List2 = []
while j!=int(X/2)+1:
    if X%j == 0:
        List2.append(j)
    j+=1
List2.append(X)

"""
TC of this is O(N/2) ~ O(N) & SC is O(k), where k is the No. of Factors/Divisors.
"""

print(List2)

# Way 3 -> Optimal Solution
l = 1
List3 = []
while l<X//l:
    if X%l==0:
        List3.append(l)
        List3.append(X//l)
    l+=1
if l == X//l:
    List3.append(X//l)


"""
TC of this is O(N/k) ~ O(N) & SC is O(k), where k is the No. of Factors/Divisors.
"""

print(sorted(List3))

# Way 3 -> Similar to Way 2, here just using sqrt
from math import sqrt

o = 1
List4 = []
while o!=(int(sqrt(X))+1):
    if X%o==0:
        List4.append(o)
        if sqrt(X) != (X//o):
            List4.append(X//o)
    o+=1
    
print(sorted(List4))
