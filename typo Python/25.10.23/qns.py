# wap to find the union of two list of integers
def union (ls1, ls2):
    l= []
    for i in ls1:
        if i not in ls2:
            ls1.append(i)
            ls =  ls1+l
            return ls

def intersection(ls1, ls2):
    lst = []
    for i in ls1:
        if i in ls2:
            lst.append(i)
    return(lst)

def symmetric_difference(ls1, ls2):
    lst1 = union(ls1, ls2)
    lst2 = intersection(ls1, ls2)  
    for i in lst2:
        if i in lst1:
            lst1.remove(i)
    return lst1

    return out
    
arr1 = [1,2,3,5]
arr2 = [2,5,90]

rel1 = union(arr1,arr2)
print(rel1)

rel2 = intersection(arr1,arr2)
print(rel2)

rel3 = symmetric_difference(arr1,arr2)
print(rel3)