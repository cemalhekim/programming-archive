# Check Permutation: Given two strings, write a method to decide if one is a permutation of the 
# other.

def check_permutation(s1: str, s2: str):
    n = 0
    if(len(s1) != len(s2)):
        return False
    for i in range(len(s1)):
        if s1[i] not in s2:
            return False
        elif s1[i] == s2[i]:
            n = n + 1
            continue    
    if n == len(s1):
        return False    
    return True 

# Test cases
print(check_permutation("abc", "cba"))  
print(check_permutation("abc", "def"))  
print(check_permutation("abc", "abcd"))  
print(check_permutation("abc", "ab"))  
print(check_permutation("abc", "a")) 
print(check_permutation("abc", "abc"))  
print(check_permutation("abc", "aab"))  
print(check_permutation("abc", "bca")) 
print(check_permutation("abc", "bac"))  
print(check_permutation("abc", "cab"))  