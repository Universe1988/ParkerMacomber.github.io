
def main():
    A = [4,10,3,2,7,1]
    p = 0
    r = len(A)
    MergeSort(A,p,r)
    print("Sorted Array: ", A)

def MergeSort(A,p,r):
    if p < r-1:
        q = (p+r)//2
        MergeSort(A,p,q)
        MergeSort(A,q + 1,r)
        Merge(A,p,q,r)

def Merge(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q

    L = [0]*(n1)
    R = [0]*(n2)

    for i in range(0, n1):
        L[i] = A[p+i]
        
    for j in range(0, n2):
        R[j] = A[q+1+j]
  
    

    i = 1
    j = 1

    for k in range(p, r):
        if L[i] <= [j]:
            A[k] = L[i]
            i = i + 1
        else: 
            j = j + 1
      

