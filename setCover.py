def setCover(V,S):
    M=[S[0]]
    U=[]
    for i in S[0]:
        U.append(i)
    while len(U)!= len(V):
        newSet = S[0]
        diff = 100
        for j in range(1,len(S)):
            count = 0
            for n in S[j]:
                if n not in U:
                    count+=1
            if 0 < count and count < diff:
                newSet = S[j]
                diff = count
        if newSet not in M and diff != 0:
            M.append(newSet)
            for n in newSet:
                if n not in U:
                    U.append(n)
        else:
            break
    return M

def multi(S):
    V=[]
    m=0
    loc = (0,0)
    for s in S:
        for i in s:
            if i not in V:
                V.append(i)
    A=[]
    
    for i in range(0,len(V)):
        A.append([])
        for j in range(0,len(V)):
            A[i].append(0)
            for s in S:
                if (i+1 in s) and (j+1 in s) and (i != j):
                    #print(i+1,j+1)
                    A[i][j]+=1
                    #print(A)
            if A[i][j] > m:
                m=A[i][j]
                loc=(i+1,j+1)
    print(A)                    
    return loc,m

if __name__ == '__main__':
    S=[[27,52,59,60,66,79],[21,22,32,44,47,78],[15,26,31,49,61,64],[12,17,43,47,61,79],[6,24,29,44,72,77],[13,20,31,38,70,79],[4,27,44,56,63,64],[2,27,30,55,70,72],[14,21,36,42,64,75],[8,11,39,61,72,74],[38,40,48,69,71,75],[11,14,38,54,68,77],[11,20,50,56,59,62],[4,18,20,24,30,71],[23,26,59,77,78,81],[7,27,47,53,54,69],[10,15,32,57,69,72],[23,43,62,72,73,75],[19,23,32,41,60,71],[13,23,46,53,58,64],[2,9,22,28,49,62],[27,48,49,68,73,80],[1,39,40,42,67,70],[5,8,36,63,78,80],[27,41,42,74,76,81],[9,23,25,51,70,80],[19,30,36,37,54,65],[7,9,14,24,60,61],[3,34,40,49,53,77],[21,31,34,35,55,60],[9,37,38,44,46,74],[5,29,31,54,62,76],[1,7,10,20,73,78],[18,33,42,46,47,62],[21,29,39,45,48,59],[13,33,34,36,52,72],[3,5,14,32,56,70],[17,18,25,55,63,77],[12,40,44,50,51,52],[13,22,24,48,65,81],[6,28,35,56,58,69],[6,26,45,47,65,70],[7,13,16,28,39,63],[10,11,51,64,65,66],[5,26,28,52,71,74],[1,34,37,43,56,81],[3,7,29,33,41,51],[5,10,12,46,48,55],[2,33,35,38,66,78],[1,6,8,46,60,68],[3,4,8,22,75,79],[14,18,45,52,58,73],[3,15,16,30,46,59],[30,40,58,61,76,78],[3,17,35,65,73,74],[29,37,57,58,79,80],[18,32,37,39,49,66],[11,16,34,47,71,80],[10,19,28,42,77,79],[11,22,41,55,58,67],[2,8,19,45,50,53],[4,26,33,57,67,68],[1,15,22,25,52,54],[13,17,32,50,68,76],[9,17,36,59,67,69],[4,12,23,35,39,54],[40,57,60,62,63,65],[6,12,20,36,41,49],[21,28,30,43,51,68],[4,9,10,34,45,76],[16,19,31,44,67,73],[15,38,41,43,45,63],[6,16,25,66,75,76],[2,12,14,16,57,81],[7,26,37,50,55,75],[15,24,35,42,50,80],[8,18,31,51,69,81],[20,21,25,53,57,74],[5,24,43,53,66,67],[1,2,17,29,64,71],[19,25,33,48,56,61]]
    #S=[[1,2,3],[1,2,4],[4,2,8],[4,2,3]]
    print(multi(S))

