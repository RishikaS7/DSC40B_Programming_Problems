import dsc40graph

def cluster_helper(u, graph, status, non_edges):
    nodes = []
    status[u] = "pending"

    for v in graph.neighbors(u):
        if (status[v] == "undiscovered" and (u, v) not in non_edges and (v, u) not in non_edges):
            nodes += cluster_helper(v, graph, status, non_edges)

    status[u] = "visited"
    nodes.append(u)
    return nodes


def cluster(graph, weights, level):
    """
    >>> edges = [("a", "b"), ("b", "c"), ("c", "d"), ("a", "d")]
    >>> graph = dsc40graph.UndirectedGraph()
    >>> for edge in edges:
    ...     graph.add_edge(*edge)
    >>> def weights(x, y):
    ...     x, y = (x, y) if x < y else (y, x)
    ...     return {
    ...         ("a", "b"): 1,
    ...         ("b", "c"): .3,
    ...         ("c", "d"): .9,
    ...         ("a", "d"): .2
    ...     }[(x, y)]

    >>> cluster(graph, weights, 0.4)
    frozenset({frozenset({'a', 'b'}), frozenset({'c', 'd'})})
    """
    status = {node: "undiscovered" for node in graph.nodes}
    clusters = []
    non_edges = []

    for edge in graph.edges:
        if weights(edge[0], edge[1]) < level:
            non_edges.append(edge)

    for node in graph.nodes:
        if status[node] == "undiscovered":
            clusters.append(frozenset(cluster_helper(node, graph, status, non_edges)))

    return frozenset(clusters)