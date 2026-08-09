

n_comparisons = 0

def main():
    filename = input("Enter a file: ")
    file = open(filename, 'r')
    A2 = file.readlines()

    bubbleSort(A2)
    print(A2)
    print (n_comparisons)

def compare_gt(x,y):
    global n_comparisons
    n_comparisons +=1
    return x > y

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range (n-i-1):
            if compare_gt(A[j], A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]

