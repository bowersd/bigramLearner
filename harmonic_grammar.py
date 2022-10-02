import random

def perturb_weights(weights):
    h = []
    for w in weights:
        p = random.gauss(w, 2) 
        if p >= 0: h.append(p)
        else: append(0)
    return h

def apply_weights(violations, weights):
    h = []
    for i in range(len(violations)):
        h.append(violations[i]*weights[i])
    return sum(h)

def select_winner(v_vector, weights):
    h = []
    floor = 0
    for i in range(len(v_vector)):
        scored = apply_weights(v_vector[i])
        if scored == floor: h.append(i)
        elif scored < floor or not floor: 
            h = [i]
            floor = scored
    if len(h) > 1: print("tied winners, selecting one at random")
    return h[random.randrange(len(h))]

