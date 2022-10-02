import harmonic_grammar as hg

def erc(v_winner, v_loser):
    h = []
    for i in range(len(v_winner)):
        if v_winner[i] > v_loser[i]: h.append(1) #W
        elif v_winner[i] < v_loser[i]: h.append(-1) #L 
        else: h.append(-0) #e
    return h

def error_detection(v_vector, weights, obs_winner):
    pred_winner = hg.select_winner(v_vector, weights)
    return pred_winner != obs_winner

def update_weights(pred_winner, obs_winner, weights, update_rate):
    ranking = erc(obs_winner, pred_winner)
    return [weights[i]+(update_rate*ranking[i]) for i in range(len(weights))]

    
