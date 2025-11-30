"""Question
You are given an undirected graph stored
1) as an adjacency list
2) as an adjacency Matrix.

Write functions to traverse this graph using the Breadth first Search approach.
As you traverse the graph store the values of the vertices in an array and return this array."""

# An adjacency list in Python
adjacency_list = {
    'A': ['B', 'F'],
    'B': ['A', 'F', 'C'],
    'C': ['B', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C', 'F'],
    'F': ['A', 'B', 'E']
}
 
def travBFS(graph, start):
    visited = {} # to keep track of visited nodes
    queue = [start] # queue to process nodes
    output = [] # list to save the traversal order
    visited[start] = True
 
    while len(queue) > 0:
        current = queue.pop(0)
        output.append(current)

        neighbours = graph[current]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited[neighbour] = True
 
    return output

print(travBFS(adjacency_list, 'A'))
