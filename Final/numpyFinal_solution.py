import numpy as np


def triangular(n):
    A = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i<j:
                A[i,j] = 1
            elif i>j:
                 A[i,j] = -1
    return np.array(A)




def dct_to_array(m,dct):
    B = np.zeros((m,m))
    for key in dct.keys():
        row, col = key   
        B[row,col] = dct[key]
    return np.array(B)





def main():
    # Part A:
    n = 3
    print(triangular(n))
    
    # Part B:
    m = 4
    dct = {(0,1):5, (1,2):7, (2,2):4, (3,0):9 , (3,2):6 }
    
    print(dct_to_array(m,dct))
    
 
    
################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()
    



