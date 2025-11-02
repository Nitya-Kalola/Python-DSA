# Recursion using Parameters

def func(X,N):
    if N==0:
        return
    print(X)
    func(X,N-1) # Change in parameter

func("Hi",5) # Prints "Hi" 5 Times

# Print 1 to N using Head Recursion

def func(A,X):
    if A>X:
        return
    print(A)
    func(A+1,X)

func(1,5)

# Print 1 to N using Tail Recursion

def func(A,X):
    if A>X:
        return
    func(A,X-1)
    print(X)

func(1,5)

# Print N to 1 using Tail Recursion

def func(A,X):
    if A>X:
        return
    func(A+1,X)
    print(A)

func(1,5)

# Print N to 1 using Head Recursion

def func(A,X):
    if A>X:
        return
    print(X)
    func(A,X-1)

func(1,5)