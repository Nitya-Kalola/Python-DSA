String = input("Enter the String: ")

def String_Palindrome(String, Start = 0, End = None):
    
    if End is None:
        End = len(String)-1
    
    if len(String) == 0:
        return f"\"{String}\" is Palindrome."
        
    if Start<End:
        if String[Start]==String[End]:
            return String_Palindrome(String,Start+1,End-1)
        return f"\"{String}\" is Not Palindrome."
    return f"\"{String}\" is Palindrome."
        
print(String_Palindrome(String))

# Time Complexity - O(N/2) ~ O(N)
# Stack Complexity - O(N/2) ~ O(N) - Stack Space