def matrixMultiplication(N, arr):
    dp = [[0]*N for _ in range(N)]
    for l in range(1,N+1):
        for i in range(1,N-l+1):
            j = i+l - 1
            if i==j:dp[i][j] = 0
            else:
                dp[i][j] = float('inf')
                for k in range(i,j):
                    dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]+arr[i-1]*arr[k]*arr[j])
    return dp[1][N-1]                
