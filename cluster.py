def cluster(graph, weights, level):
    """
    >>> def weights(x, y):
    ... x, y = (x, y) if x < y else (y, x)
    ... return {("a", "b"): 1, ("b", "c"): .3, ("c", "d"): .9, ("a", "d"): .2}[(x, y)]
    >>> cluster.cluster(graph, weights, 0.4)
    frozenset([frozenset(['a', 'b']), frozenset(['c', 'd'])])
    """