def triangle_type(side1, side2 , side3):
    a = side1
    b = side2
    c = side3
    if a**2 > b**2 + c**2 or  b**2 > a**2 + c**2 or   c**2 > a**2 + b**2:
        return 3
    elif a**2 == b**2 + c**2 or  b**2 == a**2 + c**2 or   c**2 == a**2 + b**2:
        return 2
    else:
        return 1


    
    
def main():
    '''
    You can test your implementation using the function calls here.
    These are here only to help you test your function.
    What matters is whether your triangle_type function is correct.
    '''
    result=triangle_type(3,4,5) #right
    #result=triangle_type(3,5,9) #obtuse
    #result=triangle_type(3,3,3) #acute
    print(result)
    
################################################################ 

'''
DO NOT EDIT BELOW THIS LINE
'''
if __name__ == '__main__':
    main()
