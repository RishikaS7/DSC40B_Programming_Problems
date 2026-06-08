def learn_theta(data, colors):
    max_blue = max(val for val, color in zip(data, colors) if color == 'blue')
    return max_blue


def compute_ell(data, colors, theta):
    loss = 0.0
    for val, color in zip(data, colors):
        if color == 'red' and val <= theta:
            loss += 1
        elif color == 'blue' and val > theta:
            loss += 1
    return loss


def minimize_ell(data, colors):
    best_theta = None
    best_loss = float('inf')
    for theta in data:
        loss = compute_ell(data, colors, theta)
        if loss < best_loss:
            best_loss = loss
            best_theta = float(theta)
    return best_theta


def minimize_ell_sorted(data, colors):
    n = len(data)

    blue_greater = sum(1 for color in colors if color == 'blue')
    red_less = 0
    loss = blue_greater + red_less

    best_loss = loss
    best_theta = data[0] - 1.0

    for alpha in range(n):
        if colors[alpha] == 'blue':
            blue_greater -= 1
        else:
            red_less += 1

        loss = blue_greater + red_less
        if loss < best_loss:
            best_loss = loss
            best_theta = float(data[alpha])

    return best_theta