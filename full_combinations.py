import itertools

list_of_prefix_slots = [
        ["ma"],
        ["Pi", "mag"],
        ["ka", "si"],
        ["pag"],
        ["pa"],
        ["ki"],
        ]
i = 1
with open("tagalog_prefixes.txt", 'w') as file_out:
    while i <= len(list_of_prefix_slots):
       for c in itertools.combinations(list_of_prefix_slots, i):
           for p in itertools.product(*c): file_out.write(str(p)+'\n')
       i += 1
