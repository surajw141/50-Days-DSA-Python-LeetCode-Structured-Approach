"""Minimum Window Substring: 
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
of such that every character int(including duplicates) is included in the window. 
If there is no such substring, returnthe empty string"".
The testcases will be generated such that the answer is unique."""

def minWindow(s, t):
    if t == "": return ""
    count_t , slide_window = {}, {}
    
    for c in t:
        count_t[c] = 1 + count_t.get(c, 0)
        
    need = len(count_t)
    
    have = 0
    res = [-1, -1]
    res_length = float("infinity")
    left = 0
    for right in range(len(s)):
        c = s[right]
        slide_window[c] = 1 + slide_window.get(c, 0)
        if c in count_t and slide_window[c] == count_t[c]:
            have += 1
        while have == need:
            if (right - left + 1) < res_length:
                res = [left, right]
                res_length = right - left + 1
            slide_window[s[left]] -= 1
            if s[left] in count_t and slide_window[s[left]] < count_t[s[left]]:
                have -= 1
            left += 1
            #print(s[left])
    left, right = res
    return s[left:right+1] if res_length != float("infinity") else ""
print(minWindow("ADOBECODEBANC", "ABC"))