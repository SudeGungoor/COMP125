
def build_email(firstname, lastname, entry_year):
    email = firstname[0:1] + lastname + entry_year[2:4] + '@KU.EDU.TR'
    email = email.upper()
    entry_year_int = int(entry_year)
    if str.isalpha(firstname) and str.isalpha(lastname):
        if entry_year_int >= 2001 and str.isdigit(entry_year):
            return email
    else:
        return '-1'
    if not entry_year_int >= 2001 and str.isdigit(entry_year):
        return '-2'
       
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