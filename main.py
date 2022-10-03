import harmonic_grammar
import weight_learner
import babbler
import constraints
import itertools

if __name__ == "__main__":
    cuml_dist = babbler.cnts_to_cuml_dist(*babbler.laplace(*[x[1] for x in combination_counts.combination_cnt]))
    i = 0
    while i < 1000:
        i += 1
        word = babbler.rand_babble(cuml_dist)
        #need to manage creation of inverted augments
        #may need to manage extraction of alternate orders
