# Hashing - Prestoring Value into some Data Structures like List/Dictionary/Set and Fetching it when needed.

# Question 1(Number Hashing) - [5,3,2,2,1,5,5,7,5,10] is a Global List and we have to find Frequency of Given Numbers - [10,111,1,9,5,67,2] in Global List.

# Answer ->

Nums = [5,3,2,2,1,5,5,7,5,10]
Check_Nums = [10,111,1,9,5,67,2]

Dict = dict()

for Num in Nums:
    Dict[Num] = Dict.get(Num,0) + 1
    
print(f'Frequency of Nums : {Dict}\n')

def nums_check(Dict,Check_Nums):
    Dict1 = dict()
    for i in Check_Nums:
        if i in Dict:
            Dict1[i] = Dict[i]
        else:
            Dict1[i] = 0
    return Dict1
            
print(f'Frequency of Check_Nums : {nums_check(Dict,Check_Nums)}')

# Another Approach

Nums = [5,3,2,2,1,5,5,7,5,10]
Check_Nums = [10,111,1,9,5,67,2]

hash_list = [0] * 11 # Because Nums are only lies between the 0 to 10 which is total of 11.

for i in Nums:
    hash_list[i]+=1

for i in Check_Nums:
    if i<0 or i>10:
        print(f'{i}:0',end = ", ")
    else:    
        print(f'{i}:{hash_list[i]}',end = ", ")

# Question 2(Character Hashing) - We have one String "azyxyyzaaaa", from which we have to find the frequency of the given characters - ["d","a","y","x"].

# Answer ->

string = "azyxyyzaaaa"
chars = ["d","a","y","x"]

Dict = dict()

for char in string:
    Dict[char] = Dict.get(char,0) + 1

for i in chars:
    if i in Dict:
        print(f'{i}:{Dict[i]}', end = ', ')
    else:
        print(f'{i}:0',end = ', ')

# Another Approach ->

string = "azyxyyzaaaa"
chars = ["d","a","y","x"]

hash_list = [0]*26 # becasue Total Alphabets is 26.

for i in string:
    ASCII_Value = ord(i)
    Index = ASCII_Value - 97 # - 97 Because here in string there is only small characters are used and that starts from 97 th location. So to make the First Letter as 0 we are Minuse it with 97.
    hash_list[Index]+=1
    
for i in chars:
    ASCII_Value = ord(i)
    Index = ASCII_Value - 97
    print(f'{i}:{hash_list[Index]}',end = ', ')