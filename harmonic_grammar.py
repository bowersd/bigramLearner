
def apply_weights(violations, weights):
    h = []
    for i in range(len(violations)):
        h.append(violations[i]*weights[i])
    return sum(h)

def compete(v_vector, weights):
    h = []
    floor = 0
    for i in range(len(v_vector)):
        scored = apply_weights(v_vector[i])
        if scored < floor or not floor: h = [i]
        elif scored == floor: h.append(i)
    return h

