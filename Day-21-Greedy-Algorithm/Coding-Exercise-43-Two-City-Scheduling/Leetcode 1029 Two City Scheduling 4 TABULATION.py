def twoCitySchedCost(costs):
    costs.sort(key=lambda x: x[0] - x[1])
    n = len(costs) // 2
    dp = [[float('inf')] * (n + 1) for _ in range(2*n + 1)]
    dp[0][0] = 0
    
    for i in range(1, 2*n + 1):
        for j in range(max(0, i - n), min(n, i) + 1):
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + costs[i-1][0])
            if j < i:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + costs[i-1][1])
                
    return dp[2*n][n]

print(twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))