def taylor_series_ln(x, terms):

    r = 0
    for n in range (1,terms+1):

        if n % 2 ==0:
            sign = -1
        else:
            sign = +1

        
        r = r + (x**n)/n*sign


    return r


def main():
    '''
    You can test your taylor_series_ln function using the function calls below.
    You can add more tests if you want to, but you do not have to. 
    What matters is whether your taylor_series_ln function is correct.
    '''
    
    #result = taylor_series_ln(0.8, 3)
    #result = taylor_series_ln(0.8, 5)
    #result = taylor_series_ln(0.8, 15)
    #result = taylor_series_ln(0.8, 50)
    result = taylor_series_ln(0.8, 100)
    
    print(result)
    

    
################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()
