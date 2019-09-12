"""
Implement Breadth-First Search on a Graph

"""

def BSF(graph, start, visited={}):

    # We will use a queue
    queue = deque([start])

    # Begin traversal of graph
    while queue:
        # We've seen this node
        vertex = queue.popleft()
        # Since we've visited a node, add it here
        visited.add(vertex)
        for neighbor in graph[vertex]:
            # If there's a node we haven't seen
            if neighbor not in visited:
                # Add it
                queue.append(neighbor)
    # Return what we've visited
    return visited

"""
Runtime is O(V + E)

Space is O(V)

"""
