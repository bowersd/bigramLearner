import itertools as it
import harmonic_grammar as hg
import weight_learner as wl
import babbler as b
import constraints as con
import combination_counts as cc

if __name__ == "__main__":
    cuml_dist = b.cnts_to_cuml_dist(*b.laplace(*[x[1] for x in cc.combination_cnt]))
    i = 0
    constraints = []
    weights = []
    while i < 1000:
        i += 1
        word = b.rand_babble(cuml_dist)
        #need to manage creation of inverted augments
        #may need to manage extraction of alternate orders -> not really. assuming hypothetical categorical system
        constraints, weights = con.update_constraints(constraints, weights, cc.combination_cnt[word][0], 2)
        gen = it.permutations(cc.combination_cnt[word][0], len(cc.combinations_cnt[word][0]))
        

