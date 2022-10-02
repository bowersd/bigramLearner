
def apply_weights(violations, weights):
    h = []
    for i in range(len(violations)):
        h.append(violations[i]*weights[i])
    return sum(h)

def winner(weighted_summed_violations):
    return max(weighted_summed_violations)

