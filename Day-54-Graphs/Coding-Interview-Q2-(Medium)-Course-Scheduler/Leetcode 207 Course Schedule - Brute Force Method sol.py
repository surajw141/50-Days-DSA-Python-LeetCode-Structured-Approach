from collections import deque
 
# Time complexity: O(p) where p is the number of prerequisites.
def buildAdjList(n, prerecs):
    adjList = [[] for _ in range(n)]
    for prerec in prerecs:
        toTake, firstTake = prerec
        adjList[firstTake].append(toTake)
    return adjList
# Final time complexity of buildAdjList: O(n + p)
 
# Time complexity: O(E) where E is the total number of edges in the graph, since in the worst case we will visit all edges once
def checkCycleBFS(vertex, graph):
    queue = deque()
    visited = {}
    for i in range(len(graph[vertex])):
        queue.append(graph[vertex][i])
    while queue:
        curr = queue.popleft()
        visited[curr] = True
        if curr == vertex:
            return True
        neighbours = graph[curr]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
    return False
# Final time complexity of checkCycleBFS: O(E + n) (where n is the number of vertices and E is the number of edges)
 
# Time complexity: O(n*(E+n)), as we run checkCycleBFS for each of the n vertices
def checkIfCanFinish(n, prerecs):
    adjList = buildAdjList(n, prerecs)
    hasCycle = False
    for vertex in range(n):
        hasCycle = checkCycleBFS(vertex, adjList)
        if hasCycle == True:
            return False
    return True
# Final time complexity of checkIfCanFinish: O(n+p + n*(E+n)) = O(p + n^2 + nE)