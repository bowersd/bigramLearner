def erc(v_winner, v_loser):
    h = []
    for i in range(len(v_winner)):
        if v_winner[i] > v_loser[i]: h.append(1) #W
        elif v_winner[i] < v_loser[i]: h.append(-1) #L 
        else: h.append(-0) #e
    return h

def update_weights(ranking, weights, update_rate):
    #ranking = erc(obs_winner, pred_winner)
    h = []
    for i in range(len(weights)):
        update = weights[i]+(update_rate*ranking[i])
        if update >= 0: h.append(update)
        else: h.append(0)
    return h

    
