"""Question:

Group Anagrams - Given an array of strings consisting of lower case English letters, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once."""

def group_anagrams(strings):
    #write your code here
    
    if len(strings) == 0:
        return []
    sorted_strings = [''.join(sorted(i)) for i in strings]
    hash = {}
    for i in range(len(sorted_strings)):
        if sorted_strings[i] in hash:
            hash[sorted_strings[i]].append(strings[i])
            
        else:
            hash[sorted_strings[i]] = [strings[i]]
    return list(hash.values())

#use function
print(group_anagrams(["arc", "abc", "car", "cat", "act", "acb", "atc"]))