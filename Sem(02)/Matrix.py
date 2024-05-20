# Data Visualization is important (10 Marks programming)

# Matrix :-  A statement concept where elements (numbers) are arranged in the form of row and coloumn
'''how to list from user'''

# eg = 3 4 5 6 7 8
'''To get this in form of list we will do :- '''  
lst = list(map(int,input().split()))
print(lst)

# Dimensions in array (list) :-
''' One D array :-'''
lst = [3,4,5,6,6]
out = lst[0]
print(out)

'''Two D array:- '''
lst = [[3,4],[5,7],[6,6]]
out = lst[0][0] # Here first one represents row and next one represents coloumn {it is 3 x 2 matrix}
print(out)

'''  To get this in matrix form  '''
lst = [[3,4],[5,7],[6,6]]
for i in lst:
    print(*i ,sep= '\t')   # here *i is used to get all the elements of the matrix
    '''
    Output:-
    3     4
    5     7 
    6     6
    '''



'''
Task :- 
read the array from userand convert into matrix 
'''
class matrix :
    def __init__(self,arr):
        self.arr = arr
    def validity(self,m,n):
        return len(self.arr) == m * n
    def create_matrix (self,m,n):
        self.m = []
        for i in range(0,len(self.arr),n):
            self.m.append(self.arr[i:i+n])
    def disp_matrix(self):
        for i in self.m:
            print(*i)
lst =  list(map(int,input().split()))
row,column = list(map(int,input().split()))
m = matrix(lst)
print(m.validity(row,column))

if m.validity(row,column):
    m.create_matrix(row,column)
    m.disp_matirx()
else:
    print("Invalid Dimensions")