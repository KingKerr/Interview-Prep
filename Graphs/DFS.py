"""
Implement Depth-First Search for a Graph

"""

def DFS(graph, start, visited=set()):
    # Starting node
    visited.add(start)
    # Begin traversing graph
    for neighbor in graph[start]:
        # If we hadn't seen a node
        if neighbor not in visited:
            # Make recursive call to include it
            DFS(graph, neighbor, visited)
    # Return what we've seen
    return visited

"""
Runtime is O(V + E)

Space is O(V)

"""
