def Merge(A,p,q,r):
    n1 = (q-p)+1
    n2 = r-q
    LArr = []
    RArr = []
    for i in range(n1):
        LArr[i] = A[p+i-1]
    for j in range(n2):
        RArr[i] = A[q+j]
    i = 0
    j = 0
    for k in range(p,r):
        if LArr[i]<=RArr[j]:
            A[k] = LArr[i]
            i +=1
        else:
            A[k] = RArr[j]
            j+=1
Arr = [2,5,6,3,5,7,0,5,3,5,567,34]
Merge(Arr,0,5,12)
print(Arr)

