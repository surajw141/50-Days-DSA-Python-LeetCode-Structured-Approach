"""Coding Exercise: Numbers with same consecutive differences
Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.

Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.

Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]"""

def numsSameConsecDiff(n, k):
    if n == 1:
        return [i for i in range(10)]  # Special case: single-digit numbers include 0.
 
    result = []
 
    def dfs(num, length):
        if length == n:
            result.append(num)
            return
 
        last_digit = num % 10
        # Possible next digits
        next_digits = set([last_digit + k, last_digit - k])
        for next_digit in next_digits:
            if 0 <= next_digit <= 9:
                new_num = num * 10 + next_digit
                dfs(new_num, length + 1)
 
    for i in range(1, 10):  # Starting each number with digits 1 through 9 (no leading zeros)
        dfs(i, 1)
 
    return result

# Example usage:
n = 3
k = 7
print(numsSameConsecDiff(n, k))  # Output: [181, 292, 707, 818, 929]
