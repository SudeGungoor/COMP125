def tic_tac_toe(board):
    N = len(board)
    if N >= 3:
        # each row
        for row in board:
            son = ''
            for col in row:
                son += col
            if son == 'o' * N :
                return 'o'
            if son == 'x' * N :
                return 'x'
        # each column
        for col in range(N):
            son = ''
            for row in board:
                son += row[col]
            if son == 'o' * N :
                return 'o'
            if son == 'x' * N :
                return 'x'
        # diagonal
        son = ''
        for dia in range(N):
            son += board[dia][dia]
        if son == 'o' * N :
                return 'o'
        if son == 'x' * N :
                return 'x'
        # diagonal
        son = ''
        for i in range(N):
            son += board[i][N-1-i]
        if son == 'o' * N :
                return 'o'
        if son == 'x' * N :
                return 'x'
        return '.'
    return 'Board is not valid.'
        
def main():
    '''
    You can test your tic_tac_toe implementation using the function calls here.
    These function calls are here only to help you test your function.
    What matters is whether your tic_tac_toe function is correct.
    '''
    
    board = [['.', 'x', '.', 'o'],
             ['.', 'x', 'o', '.'],
             ['.', 'x', '.', '.'],
             ['o', 'o', 'x', 'o']]

    board = [['.', 'o', 'o'],
             ['x', 'x', 'x'],
             ['o', '.', '.']]

    board = [['.', 'x', 'o'],
             ['x', 'o', 'x'],
             ['o', '.', '.']]

    board = [['.', 'x', '.', 'o'],
             ['o', 'x', 'o', '.'],
             ['.', 'x', '.', '.'],
             ['o', 'x', 'x', 'o']]
   
    board = [['.', 'x', 'o'],
             ['x', 'o', 'x'],
             ['o', '.', '.']]

    print(tic_tac_toe(board))
    
    
################################################################ 
'''
DO NOT EDIT BELOW THIS LINE
'''
if __name__ == '__main__':
    main()
