def build_email(firstname, lastname, entry_year):
    
    if firstname.isalpha()==False or lastname.isalpha()==False:
        return '-1'
    elif entry_year.isdigit() == False or int(entry_year)<2001:
        return '-2' 
    else:
        email=firstname[0].upper()+lastname.upper()+entry_year[-2:]+'@KU.EDU.TR'
        
    return email 
       
def main():
    
    
    print(build_email('John', 'Doe', '2020'))
    print(build_email('Jane', 'Smith', '2005'))
    print(build_email('John-Marcus', 'Doeington', '2010'))
    print(build_email('James', 'Cool', '1998'))

    

    
################################################################ 
'''
DO NOT EDIT BELOW THIS LINE
'''
if __name__ == '__main__':
    main()
