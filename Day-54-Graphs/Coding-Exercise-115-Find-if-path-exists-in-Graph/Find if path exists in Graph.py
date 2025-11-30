"""Coding Exercise: Find if path exists in Graph
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
The edges in the graph are represented as a 2D integer array edges,
where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination,
or false otherwise."""

from collections import deque
 
def validPath(n, edges, source, destination):
    # Create the graph as an adjacency list
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Implement BFS
    queue = deque([source])
    visited = set([source])
    
    while queue:
        current = queue.popleft()
        if current == destination:
            return True  # Found a path to the destination
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return False  # No path found

# Example usage:
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
print(validPath(n, edges, source, destination))  # Output: False
