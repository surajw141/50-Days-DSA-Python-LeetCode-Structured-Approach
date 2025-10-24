def knapSack(W, wt, val, n):
    #write code here
    prev = [0]*(W+1)
    curr = [0]*(W+1)
    for i in range(1, n+1):
        for j in range (1, W+1):
            exclude = prev[j]
            include = 0
            if wt[i-1]<=j:
                include = val[i-1]+prev[j-wt[i-1]]
            curr[j] = max(exclude, include)
        prev = curr[:]
    return curr[W]

print(knapSack(8,[8,2,5],[2,3,9],3))
