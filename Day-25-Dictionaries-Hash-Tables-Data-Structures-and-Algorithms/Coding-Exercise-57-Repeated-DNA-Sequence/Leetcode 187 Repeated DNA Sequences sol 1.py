"""Repeated DNA Sequence: 

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

•For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example:

Input: s = ”GAAAATCCCCGAAAATCCCCGAAAAAGGGTTT"

Output: [”GAAAACCCCC",”TCCCCGAAAA"]"""

def findRepeatedDnaSequences(s):
    # Given Length of a sequence = 10 
    L = 10
    n = len(s)
    
    seen, output = set(), set()
    
    for start in range(n-L+1):
        temp = s[start:start+L]
        if temp in seen:
            output.add(temp[:])
        seen.add(temp)
    return list(output)

#test function
print(findRepeatedDnaSequences("GAAAATCCCCGAAAATCCCCGAAAAAGGGTTT"))