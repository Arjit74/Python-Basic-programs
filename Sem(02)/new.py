class array:
    def __init__(self, lst):
        self.lst = lst

    def reshape(self, m, n):
        M = []
        tmp = []
        for i in self.lst:
            tmp.append(i)
            if len(tmp) == n:
                M.append(tmp)
                tmp = []
        self.lst = M

    def __add__(self, other):
        row = len(self.lst)
        col = len(self.lst[0])
        M = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                M[i][j] = self.lst[i][j] + other.lst[i][j]
        return array(M)

    def __sub__(self, other):
        row = len(self.lst)
        col = len(self.lst[0])
        M = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                M[i][j] = self.lst[i][j] - other.lst[i][j]
        return array(M)

    def __mul__(self, other):
        row1 = len(self.lst)
        col1 = len(self.lst[0])
        row2 = len(other.lst)
        col2 = len(other.lst[0])

        if col1 != row2:
            raise ValueError("Matrices cannot be multiplied due to incompatible dimensions")

        result = [[0 for _ in range(col2)] for _ in range(row1)]
        for i in range(row1):
            for j in range(col2):
                for k in range(col1):
                    result[i][j] += self.lst[i][k] * other.lst[k][j]
        return array(result)

    def disp_matrix(self):
        for i in self.lst:
            print(*i)


# Taking input for the first matrix
lst1 = list(map(int, input().split()))
r1, c1 = list(map(int, input().split()))
arr1 = array(lst1)
arr1.reshape(r1, c1)
print("\n Matrix 1")
arr1.disp_matrix()

# Taking input for the second matrix
lst2 = list(map(int, input().split()))
r2, c2 = list(map(int, input().split()))
arr2 = array(lst2)
arr2.reshape(r2, c2)
print("\n Matrix 2")
arr2.disp_matrix()

# Performing addition
if (r1, c1) == (r2, c2):
    print("\n Addition")
    addition = arr1 + arr2
    addition.disp_matrix()
else:
    print("Invalid Dimensions for addition")

# Performing subtraction
if (r1, c1) == (r2, c2):
    print("\n Subtraction")
    subtraction = arr1 - arr2
    subtraction.disp_matrix()
else:
    print("Invalid Dimensions for subtraction")

# Performing multiplication
if c1 == r2:
    print("\n Multiplication")
    multiplication = arr1 * arr2
    multiplication.disp_matrix()
else:
    print("Invalid Dimensions for multiplication")
