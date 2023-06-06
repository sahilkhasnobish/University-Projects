
def rearrange(a, p, r):
    if p < r:
        q = divide(a, p, r)
        rearrange(a, p, q-1)
        rearrange(a, q+1, r)
    return

def divide(a, p, r):
    x = a[r]
    j = p-1
    for i in range(p,r,1):
        if (a[i] < 0) and (a[j] > 0):
            j = j+1
            i, j = swap(i, j)
    swap(j+1, r)
    return j+1

def swap(x, y):
    temp = a
    x = y
    y = temp

    return x, y

a = [1,2,-3,-5,6,7,-9]

rearrange(a, 0, 6)



