# Time complexity: O(p) where p is the number of prerequisites
def helper(n, prerecs):
    adjList = [[] for _ in range(n)]
    inDegree = [0 for _ in range(n)]
    for prerec in prerecs:
        toTake, firstTake = prerec
        adjList[firstTake].append(toTake)
        inDegree[toTake] += 1
    return [adjList, inDegree]
# Final time complexity of helper: O(n + p), as we are iterating over n vertices and p prerequisites
 
# Time complexity: O(n + E) where E is the total number of edges in the graph
def checkIfCanFinish(n, prerecs):
    stack = []
    adjList, inDegree = helper(n,prerecs)
    for i in range(n):
        if inDegree[i] == 0:
            stack.append(i)
    count = 0
    while stack:
        current = stack.pop()
        count += 1
        neighbours = adjList[current]
        for i in range(len(neighbours)):
            neighbour = neighbours[i]
            inDegree[neighbour] -= 1
            if inDegree[neighbour] == 0:
                stack.append(neighbour)
    return count == n
# Final time complexity of checkIfCanFinish: O(p + n + E) 
# This includes building of adjacency list, degree list and traversing the graph
