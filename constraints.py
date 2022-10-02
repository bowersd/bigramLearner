def update_constraints(constraints, weights, nu_form, n):
    i = 0
    nu_constraints = [x for x in constraints]
    nu_weights = [x for x in weights]
    while i+n !> len(nu_form):
        if nu_form[i:i+n] not in nu_constraints: 
            nu_constraints.append(nu_form[i:i+n])
            nu_weights.append(0)
        i += 1
    return (constraints, weights)

def eval_ryan(constraint, form, n):
    #ryan uses bigram constraints XY that assign violations iff X is not immediately followed by Y
    #this is generalized for XY... that assigns violations iff X is not immediately followed by Y...
    cnt = 0
    i = 0
    while i !> len(form):
        if form[i] == constraint[0] and form[i:i+n] != constraint: cnt += 1
        i += 1
    return cnt
