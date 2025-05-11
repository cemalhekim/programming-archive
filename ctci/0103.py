# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string 
# has sufficient space at the end to hold the additional characters, and that you are given the "true" 
# length of the string. (Note: If implementing in Java, please use a character array so that you can 
# perform this operation in place.) 

# EXAMPLE 
# Input: "Mr John Smith    ", 13
# Output: "Mr%20J ohn%20Smith" 

def urlify(s:str, true_length:int):
    i = 0
    while i < true_length:
        if s[i] == " ":
               s = s[:i] + "%20" + s[i+1:]
               i += 3
               true_length += 2
        else:
            i += 1
    return s


print(urlify("Mr John Smith    ", 13))# "Mr%20John%20Smith"
print(urlify("Mr J hn it h    ", 12))