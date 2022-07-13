def matrix_transpose(A):
    N = len(A)
    a=[]
    b=[]
    for i in range(0,N):
        c = []
        for j in range (0,N):
            a = A[j][i]
            c.append(a)
        b.append(c)
    return b

def symmetric_matrix(A):
    if matrix_transpose(A) == A:
        return 1
    else:
        return -1
   
def diagonal_matrix(A):
    N = len(A)
    a = []
    for i in range(N):
        a.append([0]*N)
    for i in range(0, N):
        for j in range(0, N):
            if i == j:
                a[j][i] = A[i][j]                      
    return a

def main():
    
    A = [[1, 4, 2], 
         [2, 1, 7], 
         [1, 1, 1]]
    
    A = [[1, 2, 3], 
         [2, 2, 8], 
         [3, 8, 6]]    
    
    
    A_tran = matrix_transpose(A)
    symmetric = symmetric_matrix(A)
    diagonal = diagonal_matrix(A)
    
    print(A_tran)
    print(symmetric)
    print(diagonal)
    
    
################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()
