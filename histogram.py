# Homework 3: Programming Problem 1

def histogram(points, bins):
    """
    >>> points = [1, 2, 3, 6, 7, 9, 10, 11]
    >>> bins = [(0, 4), (4, 8), (8, 12)]
    >>> histogram(points, bins)
    [0.09375, 0.0625, 0.09375]
    """
    density_list = []
    i = 0
    for a, b in bins:
        count = 0
        while i < len(points) and points[i] < b:
            if points[i] >= a:
                count += 1
            i += 1 
        density_list.append(count / (len(points) * (b-a)))
    return density_list


