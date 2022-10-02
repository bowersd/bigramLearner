
def apply_weights(violations, weights):
    h = []
    for i in range(len(violations)):
        h.append(violations[i]*weights[i])
    return sum(h)
