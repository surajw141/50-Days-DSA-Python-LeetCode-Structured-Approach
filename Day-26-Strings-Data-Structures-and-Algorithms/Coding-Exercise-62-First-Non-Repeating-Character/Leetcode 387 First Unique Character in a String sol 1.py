"""Question:
Non repeating character - You are given a string consisting of only lower case and upper-case 
Alphabets and integers 0 to 9. Write a function that will take this string as Input and return 
the index of the first character that is non-repeating.

Try to optimise your solution:

Brute Force method : 
T=O(n^2), S=O(1)

Optimal Solution:
T=O(n), S=O(1)"""

def non_repeating_char(str):
    for i in range(len(str)):
        repeat = False
        for j in range(len(str)):
            if i!=j and str[i]==str[j]:
                repeat = True
        if repeat == False:
            return i
        
    return None

print(non_repeating_char("abaRb150"))