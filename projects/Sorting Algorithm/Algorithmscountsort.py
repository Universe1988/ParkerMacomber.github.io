def main():
    filename = input("Enter a file: ")
    file = open(filename,'r')
    A1 = file.readlines()
    A1.pop(0)
    k = max(A1)+1
    size1 = len(A1)
    B1 = [0]*size1
    n_comparisons = 0
    
    CountSorts(A1,B1,k,n_comparisons)
    print("Sorted array: ",B1)
    print(n_comparisons)

def CountSorts(A1,B1,k,n_comparisons):
    C1 = [0] *k
    size = len(A1)
    
    for j in range (0,size):
        C1[A1[j]] += 1

    for i in range(1, k):
        C1[i] += C1[i-1]
    
    for j in reversed(range(0, size)):
        B1[C1[A1[j]]-1] = A1[j]
        C1[A1[j]] = C1[A1[j]] - 1
        

