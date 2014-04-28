def eigencheck(N):
    from math import *
    from matplotlib import *
    mylist = [0.5*i for i in range(0, N)]
    counts = []
    for l in mylist:
        count = 0
        for m in mylist[0:mylist.index(l)+1]:
            if m**2 + m - l >= 0 and floor(sqrt(4*(m**2 + m - l))) - sqrt(4*(m**2 + m - l)) == 0:
                count += 1

        counts.append(count)
        hist(count)
    

    
