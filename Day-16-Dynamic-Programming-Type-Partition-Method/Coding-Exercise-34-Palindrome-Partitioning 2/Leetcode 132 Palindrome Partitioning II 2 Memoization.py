def minCut(s):
    n = len(s)
    isPalindrome = [[None]*n for _ in range(n)]
    minCuts = [[None]*n for _ in range(n)]
    
    for l in range(1,n+1):
        for i in range(n-l+1):
            j = i+l -1
            if i==j:
                isPalindrome[i][j]=True
            elif s[i] == s[j] and (j==i+1 or isPalindrome[i+1][j-1]):
                isPalindrome[i][j] = True
            else:
                isPalindrome[i][j] = False    

    def partitions(start,end):
        #base case
        if start ==end or isPalindrome[start][end]:
            return 0
        if minCuts[start][end] is not None:
            return minCuts[start][end]

        minimumCuts = end - start    

        for endIndex in range(start,end):
            if isPalindrome[start][endIndex]:
                minimumCuts = min(minimumCuts,1+partitions(endIndex+1,end))
        minCuts[start][end] = minimumCuts      
        return minCuts[start][end]    

    return partitions(0,len(s)-1)    

print(minCut("ppq"))