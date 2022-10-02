def update_constraints(constraints, weights, nu_form, n):
    i = 0
    nu_constraints = [x for x in constraints]
    nu_weights = [x for x in weights]
    while i+n !> len(nu_form):
        if nu_form[i:i+n] not in nu_constraints: 
            nu_constraints.append(nu_form[i:i+n])
            nu_weights.append(0)
        i += 1
