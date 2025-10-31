def wordBreak(s, wordDict):
    n = len(s)
    dp = [False]*n

    for i in range(n):
        for word in wordDict:
            if i<len(word)-1:
                continue
            elif s[i-len(word)+1:i+1]==word and (i==len(word)-1 or dp[i-len(word)]):
                dp[i]=True
                break
    return dp[n-1]

