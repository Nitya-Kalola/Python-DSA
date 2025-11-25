List = [21,42,46,23,85,96,23,6]

def Reverse(array,left,right):
    if left < right:
        array[left], array[right] = array[right], array[left]
        return Reverse(array,left+1,right-1)
    return array
    
print(Reverse(List.copy(),1,4))

# Time Complexity - O(N/2) ~ O(N)
# Space Complexity - O(N/2) ~ O(N) - Stack Space