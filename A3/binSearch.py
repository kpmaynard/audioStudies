import numpy as np
import math

def binSearch(x, anArr):
    found = False
    sz = np.size(anArr)
    print 'sz = %d' % (sz)
    if sz == 0 :
        return "error"
    elif sz == 1:
        if x == anArr[0] :
            found = True
            print 'item found %s' % found
        else:
            found = False
            print 'item found %s' % found
        return x
    else:
        mid = int(math.floor((sz + 1) /2 ))
        print 'mid = %d' % mid
        candidate = anArr[mid]
        print 'candidate = %d' % candidate
        if x == candidate :
            found = True
            print 'item found %s' % found
            return x
        elif x < candidate :
            binSearch(x, anArr[:mid])
        else:
            binSearch(x, anArr[mid:])
