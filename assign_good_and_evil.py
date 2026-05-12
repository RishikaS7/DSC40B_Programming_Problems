import dsc40graph

def assign_good_and_evil(graph):
    """
    >>> example_graph = dsc40graph.UndirectedGraph()
    >>> example_graph.add_edge('Michigan', 'OSU')
    >>> example_graph.add_edge('USC', 'OSU')
    >>> example_graph.add_edge('USC', 'UCB')
    >>> example_graph.add_node('UCSD')
    >>> assign_good_and_evil(example_graph)
    {'OSU': 'good', 'Michigan': 'evil', 'USC': 'evil', 'UCB': 'good', 'UCSD': 'good'}
    """
    labels = {}

    for node in graph.nodes:
        if node not in labels:
            labels[node] = 'good'
            queue = [node]

            while queue:
                current = queue.pop(0)

                if labels[current] == 'good':
                    status = 'evil'
                else:
                    status = 'good'

                for neighbor in graph.neighbors(current):

                    if neighbor not in labels:
                        labels[neighbor] = status
                        queue.append(neighbor)
                    elif labels[neighbor] != status:
                        return None
    return labels


 