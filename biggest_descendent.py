import dsc40graph

def biggest_descendent(graph, root, value):
    """
    >>> edges = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 8), (4, 9), (3, 6), (3, 7)]
    >>> g = dsc40graph.DirectedGraph()
    >>> for edge in edges: g.add_edge(*edge)
    >>> value = {1: 2, 2: 1, 3: 4, 4: 8, 5: 5, 6: 2, 7: 10, 8:3, 9: 9}
    >>> biggest_descendent(g, 1, value)
    {1: 10, 2: 9, 3: 10, 4: 9, 5: 5, 6: 2, 7: 10, 8: 3, 9: 9}
    """
    status = {node: 'undiscovered' for node in graph.nodes}
    result = {}
    for node in graph.nodes:
        if status[node] == 'undiscovered':
            dfs(graph, node, value, status, result)
    return result

def dfs(graph, u, value, status, result):
    status[u] = 'pending'
    for v in graph.neighbors(u):
        if status[v] == 'undiscovered':
            dfs(graph, v, value, status, result)
    status[u] = 'visited'

    best = value[u]
    for v in graph.neighbors(u):
        best = max(best, result[v])
    result[u] = best
