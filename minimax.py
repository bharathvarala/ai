#game search - minimax
import math
def minimax(curDepth,nodeIndex,maxTurn,scores,targetDepth):
    if curDepth == targetDepth:
        return scores[nodeIndex]
    if maxTurn:
        return max(minimax(curDepth+1,nodeIndex*2,False,scores,targetDepth),minimax(curDepth+1,nodeIndex*2+1,False,scores,targetDepth))
    else:
        return min(minimax(curDepth+1,nodeIndex*2,True,scores,targetDepth),minimax(curDepth+1,nodeIndex*2+1,True,scores,targetDepth))

scores = [2,-1,3,5]
t = math.log(len(scores),2)
print(minimax(0,0,False,scores,t))
