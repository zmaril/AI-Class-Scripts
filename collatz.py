def next(n): # computes next term in the sequence
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1

history = [0,1]
for i in range(2,1000000):
    num_terms = 0
    num = i
    done = False
    while num > 1 and not done:
        num = next(num)
        if num < len(history): # number has been hit previously,
            # so the length of the rest of the path is known.
            num_terms += history[num]
            done = True
        num_terms += 1
    history.append(num_terms)

print history.index(max(history))
