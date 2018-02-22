def place_words(corp):

    corp = [x.upper() for x in corp]
    global corpus
    corpus = corp[:]
    return main(corp)

def check2(val):

    t = []
    k= []
    ch= []
    va = []
    global corpus
    for x in corpus:
        ch.append(x[0:len(val)])

    for x in xrange(len(val)):
        for y in xrange(len(val)):
            t.append(val[y][x] )
    for x in val:
        x = str(x)
        va.append(x[0:len(val)])
    for x in xrange(len(val)):
        k.append(''.join(t[len(val)*x : (len(val)*x)+len(val)]))

    return set(k + va).issubset(ch)
def main(listo):
    cop = listo[:]
    n = len(listo[1])
    copy = []
    run = []
    copy.append([])
    for x in cop:
        if check2(run + [x]):
            copy[-1].append(x)
    while len(run) < n:
        if copy[0] == [] :
            return False
        elif copy[-1] == [] and copy[-2] == []:
            run = []
            copy = copy[0:1]
            run.append(copy[-1][0])
            del copy[-1][0]
            copy.append([])
        elif copy[-1] == []:
            del copy[-1]
            del run[-1]

            run.append(copy[-1][0])
            del copy[-1][0]
            copy.append([])
        elif  copy[-1] == [] and len(run) <n :
            run = []
            copy = copy[0:1]
            run.append(copy[-1][0])
            del copy[-1][0]
        else:
            if len(copy[-1]) < n:

                run.append(copy[-1][0])
                del copy[-1][0]
                copy.append([])
            else:
                run.append(copy[-1][0])
                del copy[-1][0]
                copy.append([])

        if check2(run) and len(run) == n:

            return run
        a =  [y for y in listo if y not in run]
        for x in  a :
            if check2(run+[x]):
                copy[-1].append(x)
