# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you 
# cannot use additional data structures? 

def is_unique(s: str):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

# Test cases
print(is_unique("abcdefg"))  # True
print(is_unique("abcdeafg"))  # False
print(is_unique(""))  # True    
print(is_unique("a"))  # True
print(is_unique("ab"))  # True
print(is_unique("aa"))  # False
print(is_unique("abcde"))  # True
print(is_unique("abcdeaf"))  # False
print(is_unique("abcdefghijklmnopqrstuvwxyz"))  # True

