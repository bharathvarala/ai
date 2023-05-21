#game search alpha-beta pruning

import math
MAX = 1000
MIN = -1000
def minimax(depth,nodeIndex,maxPlayer,values,alpha,beta):
    if depth == int(math.log(len(values),2)):
        return values[nodeIndex]
    
    if maxPlayer:
        best = MIN
        for i in range(2):
            val = minimax(depth+1,nodeIndex*2+i,False,values,alpha,beta)
            best = max(best,val)
            alpha = max(alpha,best)
            if beta<=alpha:
                break
        return best
    else:
        best = MAX
        for i in range(2):
            val = minimax(depth+1,nodeIndex*2 + i,True,values,alpha,beta)
            best = min(best,val)
            beta = min(best,beta)
            if beta<=alpha:
                break
        return best
v = [1,2,3,4,5,6]
print(minimax(0,0,False,v,MIN,MAX))
