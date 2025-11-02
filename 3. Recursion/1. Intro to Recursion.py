# Recursion - When Function calls itself
count = 0
def greet(): # It's called as Infinite Recursion. and it leads to Stack Overflow Error.
    print("Hello")
    count+=1
    greet()

greet()

# Stack Overflow Occurs when the Stack space got filled completely.
# And Stack space got fill every time when the function will be calling. It can handle 997 or 998 calls Mostly in Python.

# Head Recursion

count = 0

def greet(count): # It's called Head Recursion - Do job first and then Calling a Function
    
    if count==4:
        return
    
    print("Hello") # Job First
    count+=1

    greet(count) # Then Calling a Function
        
greet(count)

# Tail Recursion(Back Tracking)

count = 0

def greet(count): # It's called Tail Recursion - Calling a Function Fist and then Do job
    
    if count==4:
        return
    
    count+=1

    greet(count) # Calling a Function First

    print("Hello") # Then Do Job

greet(count)

# Recursion Tree - Make it for Both Head and Tail recursion to Visualize the Process of your code.

# TC -> O(n)
# SC -> O(n)