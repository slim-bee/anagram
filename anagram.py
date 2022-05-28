# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


#Python code to check if two strings are anagrams of each other or not using sorted()

def isAnagram(a, b):
    
    #Unequal Length strings cannot be anagrams
    if len(a) != len(b):
        return False
    
    #sort the first string
    first = sorted(a)
    #sort the second string
    second = sorted(b)
    
    #check if both the strings are same
    if first == second:
        return True
    else:
        return False
    
#driver code
ans = isAnagram("hello","check")
print(ans)


