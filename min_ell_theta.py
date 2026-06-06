def learn_theta(data, colors):
    max_blue = max(x for x, c in zip(data, colors) if c == 'blue')
    return max_blue


def compute_ell(data, colors, theta):
    loss = 0.0
    for x, c in zip(data, colors):
        if c == 'red' and x <= theta:
            loss += 1
        elif c == 'blue' and x > theta:
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

    blue_theta = sum(1 for c in colors if c == 'blue')
    red_theta = 0
    loss = blue_theta + red_theta

    best_loss = loss
    best_theta = float(data[0])

    for alpha in range(n):
        if colors[alpha] == 'blue':
            blue_theta -= 1
        else:
            red_theta += 1

        loss = blue_theta + red_theta
        if loss < best_loss:
            best_loss = loss
            best_theta = float(data[alpha])

    return best_theta