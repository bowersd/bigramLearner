
def erc(v_winner, v_loser):
    h = []
    for i in range(len(v_winner)):
        if v_winner[i] > v_loser[i]: h.append(1) #W
        elif v_winner[i] < v_loser[i]: h.append(-1) #L 
        else: h.append(-0) #e
    return h
