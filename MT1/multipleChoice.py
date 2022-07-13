def decimal_deduction(correct,wrong):
    
    r = (correct * 4 ) - wrong
    if r < 0:
        r = 0
    return r


def whole_deduction(correct,wrong):
    point=correct * 4
    if wrong/4 > 1:
        point = int(correct * 4- 4 * ((wrong-(wrong % 4))/4))
    if point < 0:
        point = 0
    return point

def main():
    
    '''
    You can test your implementations using the function calls here.
    These are here only to help you test your functions.
    What matters is whether your decimal_deduction and 
    whole_deduction functions are correct.
    ''' 
    correct = 24
    wrong = 1
    
    #correct = 19
    #wrong = 5
    
    #correct = 17
    #wrong = 6
    
    grade1 = decimal_deduction(correct,wrong)
    grade2 = whole_deduction(correct,wrong)
    
    
    print('Result for Decimal Deduction is:', grade1)
    print('Result for Whole Deduction is:', grade2)
    
   
################################################################ 

'''
DO NOT EDIT BELOW THIS LINE
'''
if __name__ == '__main__':
    main()

