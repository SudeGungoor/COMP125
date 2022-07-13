def letter_to_number(letter):
    if letter == 'A' or letter == 'B' or letter == 'C':
        return 2
    elif letter == 'D' or letter == 'E' or letter == 'F':
        return 3
    elif letter == 'G' or letter == 'H' or letter == 'I':
        return 4
    elif letter == 'J' or letter == 'K' or letter == 'L':
        return 5
    elif letter == 'M' or letter == 'N' or letter == 'O':
        return 6
    elif letter == 'P' or letter == 'Q' or letter == 'R' or letter == 'S':
        return 7
    elif letter == 'T' or letter == 'U' or letter == 'V':
        return 8
    elif letter == 'W' or letter == 'X' or letter == 'Y' or letter == 'Z':
        return 9
    
def phone_converter(phone_alpha):
    '''
    Or you could define a dictionary instead of a helper function:
    char2int = {'A':2, 'B':2, 'C':2,
            'D':3, 'E':3, 'F':3,
            'G':4, 'H':4, 'I':4,
            'J':5, 'K':5, 'L':5,
            'M':6, 'N':6, 'O':6,
            'P':7, 'Q':7, 'R':7, 'S':7,
            'T':8, 'U':8, 'V':8,
            'W':9, 'X':9, 'Y':9, 'Z':9}
    '''
    
    if (phone_alpha[0] == '0'):
        return '-1'
    elif(len(phone_alpha)!=12):
        return '-2' 
    else:
        new_s = ''
        for i in range(3):
            c = phone_alpha[i]
            if c.isnumeric():
                new_s += c
            elif c.isalpha():
                new_s += str(letter_to_number(c.upper()))
            else:
                return '-2'
                
        c = phone_alpha[3]
        if c != '-':
            return '-2'
        else:
            new_s += '-'
            
        for i in range(4,7):
            c = phone_alpha[i]
            if c.isnumeric():
                new_s += c
            elif c.isalpha():
                new_s += str(letter_to_number(c.upper()))
            else:
                return '-2'
                
        c = phone_alpha[7]
        if c != '-':
            return '-2'
        else:
            new_s += '-'
            
        for i in range(8,12):
            c = phone_alpha[i]
            if c.isnumeric():
                new_s += c
            elif c.isalpha():
                new_s += str(letter_to_number(c.upper()))
            else:
                return '-2'
            
    return new_s 
def main():
    '''
    You can test your phone_converter via the function calls below.
    You can add more tests if you want to, but you do not have to. 
    You will not be graded on what is inside your main() function, but
    make sure that it does not cause a syntax error.
    '''
    print(phone_converter('555-GET-FOOD'))
    print(phone_converter('310-EaT-MeaT'))
    print(phone_converter('12E-456-789T'))
    print(phone_converter('444-EAT-CHICKEN'))
    print(phone_converter('444EATMEAT'))
    print(phone_converter('090-EAT-MEAT'))   
    

    
################################################################ 
'''
DO NOT EDIT BELOW THIS LINE
'''
if __name__ == '__main__':
    main()
