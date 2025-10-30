def minCut(s):
    n = len(s)
    isPalindrome = [[False]*n for _ in range(n)]
    dp = [0]*n

    for l in range(1,n+1):
        for i in range(0,n-l+1):
            j = i+l-1
            if i==j:isPalindrome[i][j]=True
            elif s[i]==s[j] and (j==i+1 or isPalindrome[i+1][j-1]):
                isPalindrome[i][j] = True
            else:
                isPalindrome[i][j] = False

    for end in range(n):
        minCuts = end
        for start in range(end+1):
            if isPalindrome[start][end]:
                if start ==0:
                    minCuts =0
                else:
                    minCuts = min(minCuts,1+ dp[start-1])
        dp[end]=minCuts
    return dp[n-1]                    

print(minCut("ppq"))