def findTheWinner(n, k):
    
    survivor = 0
    
    for i in range(2, n+1):
        survivor = (survivor + k) % i
    return survivor + 1
print(findTheWinner(6, 5))