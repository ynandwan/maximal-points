import random 


def bsearch(p,l,start=0,end=None,key=lambda x: x):
    if end == None:
        end = len(l)
    #
    n = end - start + 1


def swap(l,i,j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp
#
def partition(l,start,end,key,pi):
    swap(l,pi,end)
    #this ensures pivot is at end
    pivot = key(l[end])
    left_c = start
    right_c = end 
    while left_c < right_c:
        while ((left_c < right_c) and (key(l[left_c]) <= pivot)):
            left_c += 1
        #
        while ((right_c > left_c) and (key(l[right_c]) >= pivot)):
            right_c -= 1
        #
        if left_c != right_c:
            swap(l,left_c,right_c)
    #
    swap(l,right_c,end)
    return right_c 

#l = list(range(0,10)) + list(range(10,0,-1))
def quicksort(l,start=0,end=None,key=lambda x: x):
    if end == None:
        end  = len(l) - 1 
    #
    n = end - start + 1
    if n <= 1:
        return
    #
    if n == 2:
        if key(l[start]) > key(l[end]):
            swap(l,start,end)
        #
        return 
    #
    pi = random.randint(start,end)
    pi = partition(l,start,end,key,pi)
    quicksort(l,start,pi-1,key)
    quicksort(l,pi+1,end,key)

    
    
