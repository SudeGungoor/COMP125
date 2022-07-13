def rowwise_avg(A):
    num_rows = len(A)
    num_cols = len(A[0])
    my_list=[]
    for i in range(num_rows):
        total = 0
        for j in range(num_cols):
            total += A[i][j]
        my_list.append(total/num_rows)
    return my_list
    


def unique_elements(A):
    num_rows = len(A)
    num_cols = len(A[0])
    my_list2=[]
    for i in range(num_rows):
        for j in range(num_cols):
            if A[i][j] not in my_list2:
                my_list2.append(A[i][j])
    return my_list2

    
def create_new_mat(A):
    
    num_rows = len(A)
    num_cols = len(A[0])
   
    B = []  # create a matrix with all zeros
    for i in range(num_rows):
        row = [0] * num_cols
        B.append(row) 
        
    for i in range(num_rows):
        for j in range(num_cols):
            if (i+j) % 2 != 0:
                B[i][j] = A[i][j] - 1
            else:
                B[i][j] = A[i][j] + 1
    return B


def main():
    A = [[2,5,5,1],
         [6,0,1,0],
         [4,4,6,2],
         [1,8,2,5]]
    # Part A:
    print(rowwise_avg(A))
    
    # Part B:
    print(unique_elements(A))
    
    # Part C:
    print(create_new_mat(A))
    

    
################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()
    