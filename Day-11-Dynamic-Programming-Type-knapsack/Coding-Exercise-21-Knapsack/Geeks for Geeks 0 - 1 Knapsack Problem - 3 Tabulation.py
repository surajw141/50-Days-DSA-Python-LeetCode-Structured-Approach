def knapSack(W, wt, val, n):
    # code here
    dp = [[0]* (W+1) for _ in range(n+1)]
    for i in range (1, n+1):
        for j in range(1, W+1):
            exclude = dp[i-1][j]
            include = 0
            if wt[i-1]<=j:
                include = val[i-1]+dp[i-1][j-wt[i-1]]
            dp [i][j] = max(exclude, include)
    return dp[n][W]

print(knapSack(8,[8,2,5],[2,3,9],3))
