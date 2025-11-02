# Time Complexity(denoted by Big-O Notation -> O(N)) - Rate of time increases with respect to the Input Size.

"""
Types of Time Complexity
- 1) Worst Case(also called Upper Bound) - (Big-O =>denoted by O(N)), Where N is Time Taken to Execute the Code
- 2) Average Case - denoted by (Theta => θ(N))
- 3) Best Case(also called Lower Bound) - denoted by (Omega => Ω(N))
"""

"""
Rules to Calculate Time Complexity.
- 1) Always Calculate Worst Case Time Complexity. (E.g. Code Execution Time for 10, 1000, 1000000 Input Size, then Consider 1000000 Input Size)
    - If the TC of the Worst Case is best then it is always best for Average(E.g. 1000) and Best(E.g. 10) Case.
    - E.g. If Total 1000 users gonna use website... and if it performs well then it can easily handle the 500 or 50 User.
    
- 2) Avoid the Constant Terms. (E.g. 8N^6 + 3N^3 + 15, So Avoid 15, 3N^3 and Coefficient of N^6, Just Consider N^6)
    - Because as we are focusing on Rate then we just have to focus on Largest Input Size and Neglect Less Input size than Largest Input Size.

- 3) Avoid Lower Bound(Best Case)
"""

"""
Example 1:

Code:
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("Hello")

Time Complexity:

    For i = 1, j = 1,2,3,....,n -> n Time
    For i = 2, j = 1,2,3,....,n -> n Time
    .
    .
    For i = n, j = 1,2,3,....,n -> n Time

    - Which means n Time + n Time + n Time +...+ n Time for i = n Times, it Executes -> n*n=n^2 -> O(n^2).
    
"""

"""
Example 2:

Code:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("Hello")

Time Complexity:

    For i = 1, j = 1 -> 1 Time
    For i = 2, j = 1,2 -> 2 Time
    For i = 3, j = 1,2,3 -> 3 Time
    .
    .
    For i = n, j = 1,2,3,...,n -> n Time

    - Which means 1 Time + 2 Time +3 Time +...+ n Time for i = n Times, it Executes -> n(n+1)/2 ->((n^2)/2 + n/2),
    so We just have to extract Largest Term for Time Complexity & Neglect Constant Term also... so Time COmplexity will be O(n^2), which is similar to Previous Example's Time Complexity.

"""

# Space Complexity(also denoted by Big-O Notation - O(N)) - Auxiliary Space + Input Space

"""
Auxiliary Space - Extra Space used to solve the Problem.
                - E.g. Temporary variables, Extra arrays, or Data Structures used during the algorithm's execution.

Input Space - Set of all possible inputs a function or model can receive.
            - E.g. If a function takes a single integer as input, the input space would be all possible integers.

Combined Example:

    Code:
        x,y,z = 1,2,3
        p = x+y+z
        print(p)

    Input Space: x,y,z = 1,2,3, Because x,y,z are actual input storing variables.

    Auxiliary Space: p = x+y+z, Because p is a Temporary Variable that used to store Output of the Problem.

"""

"""
Code:
    x,y,z = 1,2,3
    x = x+y+z
    print(x)

    Note: Don't Change the Input unless asked, instead make another variable to store Output.
    
"""

"""
Example:
    Suppose we are taking list/array that can store N values... then its Space Complexity will be O(N).

"""
