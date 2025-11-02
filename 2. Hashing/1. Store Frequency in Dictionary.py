# Store Frequency in Dictionary

# Method 1
Nums = [1,3,2,4,2,4,4,1,2,4,6,7,9,5,2,5,6,4,2,8,3,3,9,3,1]

Dictionary = dict()

for i in range(0,len(Nums)): # -> O(N) - As it runs for N times
    if Nums[i] not in Dictionary: # -> O(1)
        Dictionary[Nums[i]] = 1 # -> O(1)
    else:
        Dictionary[Nums[i]]+=1 # -> O(1)
        
print(Dictionary)

"""
Time Complexity of this will be O(N), where N is Number of Total Elements in List & Space Complexity also will be O(N), where N is Number of Unique Elements in List.
"""

# Method 2 - Also works same as above code. It gives output just in few lines of code.
Dict = {}

for i in range(0,len(Nums)): # -> O(N) - As it runs for N times
    Dict[Nums[i]] = Dict.get(Nums[i],0) + 1 # -> O(1) - For get() method
print(Dict)

"""
So Time Complexity of this also will be O(N), where N is Number of Total Elements in List & Space Complexity also will be O(N), where N is Number of Unique Elements in List.
"""
