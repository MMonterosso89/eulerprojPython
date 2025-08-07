def collatz_seq(start_num,verbose=False):
    terms = 1
    log = []
    sequence = start_num
    while sequence > 1:
        if sequence % 2 == 0:
            terms+=1
            sequence = int(sequence / 2)
            log.append(sequence)
        else:
            terms+=1
            sequence = int((3*sequence)+1)
            log.append(sequence)
    if verbose == True:
        return (start_num, terms, log)
    else:
        return terms


sample_seq = collatz_seq(13)


collatz_dict = {}
for val in range(0,int(1e6+1)):
    collatz_dict[val] = collatz_seq(val)

max_key = max(collatz_dict, key=lambda k: collatz_dict[k])


#837799

longest_seq = collatz_seq(837799, verbose=True)