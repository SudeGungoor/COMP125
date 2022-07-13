def compute_series(x,terms):
    result=1
    for i in range(1,terms):
        a=i*2
        if i%2==0:
            sign=+1
        else:
            sign=-1
        factorial=1
        for j in range(1,a+1):
            factorial = factorial*j
        result = result + (sign*x**a)/factorial
    return result  
    
    
    
    
def main():
    
    '''
    You can test your implementations using the function calls here.
    These are here only to help you test your functions.
    What matters is whether your compute_series function is correct.
    ''' 
    
    #result=compute_series(1,3)
    #result=compute_series(1,5)
    #result=compute_series(1,20)
    result=compute_series(1,100)

    print(result)
        
################################################################ 

'''
DO NOT EDIT BELOW THIS LINE
'''
if __name__ == '__main__':
    main()


