

def wordBreak(s, wordDict):
    n = len(s)
    dp = [-1]*n
    def checkBuild(i):
        if i <0: return True

        if dp[i] != -1 : return dp[i]

        for word in wordDict:
            if s[i-len(word)+1:i+1] == word and checkBuild(i-len(word)):
                dp[i] = True
                return dp[i]
        dp[i] = False        
        return dp[i]       

    return checkBuild(n-1)

