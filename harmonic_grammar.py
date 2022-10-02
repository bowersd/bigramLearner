
def apply_weights(violations, weights):
    h = []
    for i in range(len(violations)):
        h.append(violations[i]*weights[i])
    return sum(h)

def best_score(weighted_summed_violations):
    return max(weighted_summed_violations)

def compete(v_vector, weights):
    h = []
    for v in v_vector:
        h.append(apply_weights(v, weights))
    return best_score(h)
