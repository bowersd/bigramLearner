import random

def laplace(*cnts):
    return [c+1 for c in cnts]

def cnts_to_cuml_dist(*cnts):
    h = []
    total = sum(cnts)
    cur = 0
    for c in cnts:
        cur += c/total
        h.append(cur)
    return h

def rand_babble(cuml_dist):
    i = 0
    prev = 0
    target = random.random()
    while cuml_dist[i] < target:
        prev = i
        i += 1
    return prev
