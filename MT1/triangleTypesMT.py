def triangle_typeMT(a,b,c):
    if a + b > c and a + c > b and b + c > a:
       if a == b  and b == c:
           return 1
       elif a == b or b ==c or a ==c:
           return 2
       else:
           return 3
    else:
        return -1
def main():
    
    '''
    You can test your implementations using the function calls here.
    These are here only to help you test your functions.
    What matters is whether your triangle_typeMT function is correct.
    ''' 
    
    result=triangle_typeMT(8,8,6)
    #result=triangle_typeMT(5,7,6)
    #result=triangle_typeMT(6,3,2)
    #result=triangle_typeMT(4,4,4)

    print(result)
    

################################################################ 

'''
DO NOT EDIT BELOW THIS LINE
'''
if __name__ == '__main__':
    main()

    

