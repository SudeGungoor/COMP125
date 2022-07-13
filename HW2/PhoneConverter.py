
def phone_converter(phone_alpha):
    d =  {'A':'2','B':'2','C':'2','D':'3','E':'3','F':'3' ,'G':'4','H':'4', 'I':'4', 'J':'5', 'K':'5','L':'5','M':'6','N':'6','O':'6','P':'7','Q':'7','R':'7','S':'7','T':'8','U':'8','W':'9','X':'9','Y':'9','Z':'9'}
    liste = list(phone_alpha) 
    son_liste = []
    if len(liste) != 12 or liste[3] != '-' or liste[7] != '-':
        return -2
    elif liste[0] == '0':
        return -1 
    for i in liste:
        if i.isalpha():
            i = d[i.upper()]
        son_liste.append(i)
    return ''.join(son_liste)
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