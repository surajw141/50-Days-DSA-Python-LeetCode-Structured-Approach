"""Question

You are given a graph with n vertices. To indicate the connections in the graph you are given an array 
edges whose each element is an array of the form [u,v]. [u,v] indicates that there is an
edge between u and v where u and v denote two vertices or nodes. Write a function that takes in 'n' 
and the 'edges' array and returns the number of connected components in the graph."""

def build_adj_list(n, edges):
    # Initialize adjacency list with empty lists for each vertex
    adj_list = [[] for _ in range(n)]
    
    # Add edges to adjacency list
    for edge in edges:
        node1 = edge[0]  # first node of edge
        node2 = edge[1]  # second node of edge
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
    
    return adj_list
 
def dfs(graph, vertex, visited):
    # Mark vertex as visited
    visited[vertex] = True
    
    # Get neighbors of current vertex
    neighbors = graph[vertex]
    
    # Visit all unvisited neighbors
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
 
def count_components(n, edges):
    # Build adjacency list
    graph = build_adj_list(n, edges)
    
    # Initialize visited set
    visited = {}
    
    count = 0
    for vertex in range(n):
        if vertex not in visited:
            count += 1
            dfs(graph, vertex, visited)
    
    return count
 
n = 7  # vertices 0, 1, 2, 3, 4, 5, 6
edges = [[0,1],[1,2],[3,4],[5,6]]
print(count_components(n, edges))