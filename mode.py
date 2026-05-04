def mode(numbers):
    """
    >>> numbers = [4, 5, 8, 3, 4, 2, 4, 5, 5, -2]
    >>> mode(numbers)
    4
    """
    counts = {}
    for i in numbers:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    max_val = max(counts.values())
    for j in counts:
        if counts[j] == max_val:
            return j