def new_sort(n):
    if len(n)<=1:
        return n

    mid = len(n) // 2
    L = n[:mid]
    R = n[mid:]
    left_mid = len(L)//2
    right_mid = len(R) // 2

    partition1 = n[:left_mid]
    partition2 = n[left_mid:]
    partition3 = n[:right_mid]
    partition4 = n[right_mid:]

    new_sort(partition1)
    new_sort(partition2)
    new_sort(partition3)
    new_sort(partition4)

    result = merge(partition1,partition2,partition3,partition4)
    return result;

def merge(A,B,C,D):
    result = []
    i = 0
    j = 0
    n = 0
    x = 0
    while i<len(A) or j<len(B) or n<len(C) or x<len(D):
        if i == len(A):
            result.append(B[j])
            j+=1
        elif (j==len(B)):
            result.append(A[i])
            i+=1
        elif A[i]<=B[j]:
            result.append(A[i])
            i+=1
        elif B[j]>A[i]:
            result.append(B[j])
            j+=1


    return


def algorithm(n):
    i=0;
    j=0
    x=0
    while(i < n/2):
        i+=1
    while (j < n/2):
        j+=1
    while (x < n/2):
        x+=1
    return



