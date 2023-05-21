#constraint satisfaction
def isPlace(i,j):
    for k in range(i):
        if x[k]==j or abs(i-k) == abs(x[k]-j):
            return False
    return True

def nQueens(curr_q,n):
    for col in range(n):
        if isPlace(curr_q,col):
            x[curr_q] = col
            if curr_q == n-1:
                print(*x)
            else:
                nQueens(curr_q+1,n)
nQueens(0,4)
