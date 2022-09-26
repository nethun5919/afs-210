
nlist = [55 ,  31 ,  26 ,  20 ,  63 ,  7 ,  51 ,  74 ,  81 ,  40 ]

def mergeSort(nlist):
    print("Splitting ",nlist)
    # insert your code to complete the mergeSort function
    if len(nlist) > 1:
        left_nlist = nlist[:len(nlist)//2]
        right_nlist = nlist[len(nlist)//2:]
        
        mergeSort(left_nlist)
        mergeSort(right_nlist)

        nlist = merge(nlist, left_nlist, right_nlist)

    print("Merging ",nlist)
def merge(nlist,lefthalf,righthalf):

    i= 0
    j= 0
    k= 0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1
    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1
    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    return nlist

print(nlist)
mergeSort(nlist)
print(nlist)