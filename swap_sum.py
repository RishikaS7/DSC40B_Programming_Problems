# Homework 3:  Programming Problem 2

def swap_sum(A, B):
    """
    >>> A = [1, 6, 50]
    >>> B = [4, 24, 35]
    >>> swap_sum(A, B)
    (1, 0)
    """
    check = sum(B) - sum(A) - 10
    if check % 2 != 0:
        return None
    target = check // 2
    a_i = 0
    b_j = 0
    while a_i < len(A) and b_j < len(B):
        current = B[b_j] - A[a_i]
        if current == target:
            return (a_i, b_j)
        elif current < target:
            b_j += 1
        else:
            a_i += 1
    return None
