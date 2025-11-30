"""Coding Exercise: Number of Provinces
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected,
and isConnected[i][j] = 0 otherwise.
Return the total number of provinces."""

def findCircleNum(isConnected):
    def dfs(city):
        """Perform DFS to mark all cities in the same province as visited."""
        for neighbor, is_connected in enumerate(isConnected[city]):
            if is_connected and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)
    
    n = len(isConnected)
    visited = set()
    provinces = 0
    
    for city in range(n):
        if city not in visited:
            dfs(city)
            provinces += 1  # Found a new province
    
    return provinces
# Example usage:
isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
print(findCircleNum(isConnected))  # Output: 2
