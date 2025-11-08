"""Isomorphic Strings - Given two strings s and t, determine if they are isomorphic. Two strings s and t are 
if the characters in s can be replaced to get t. All occurrences of a character must be replaced with another 
character while preserving the order of characters. No two characters may map to the same character, but a character
may map to itself. s and t consist of any valid ascii character"""

def isomorphic_strings(s,t):
    if len(s) != len(t):
        return False
    s_hash, t_hash = {}, {}
    for i in range(len(s)):
        char_s, char_t = s[i], t[i]
        if char_s not in s_hash:
            s_hash[char_s] = char_t
            
        if char_t not in t_hash:
            t_hash[char_t] = char_s
            
        if s_hash[char_s] != char_t or t_hash[char_t] != char_s:
            return False
        
    return True

