def read_temperatures(filename):
    file = open("ANKARA.txt" , "r")
    x = []
    for i in file:
        a = i.split(" ")
        x2 = []
        for i2 in a:
            if i2.isdigit() == True or "." in i2:
                if '.' in i2:
                    
                    i2 = i2.strip("\n")
               
                    x2.append(float(i2)) 
                else:
                    i2 = i2.strip("\n")
               
                    x2.append(int(i2)) 
        x.append(x2)
    file.close()
    return x

def delete_year(data, year):
    x = []
    for i in data:
        if year not in i:
            x.append(i)
    return x 



def monthly_averages(data, year):
    x = []
    for i in range(1,13):
        a = 0
        b = 0
        for j in data:
            if j[0] == i and j[2] == year and j[3]!= -99:
                a += j[3]
                b += 1
        x.append(a/b)
    return x
            
            


def main():
    """
    The code given here is for you test your functions. When submitting, 
    make sure the code you leave under main() does not cause a syntax error.
    """
    #istanbul_data = read_temperatures("ISTANBUL.txt")
    #print(istanbul_data)
    ankara_data = read_temperatures("ANKARA.txt")
    print(ankara_data)
    
    #print(delete_year(istanbul_data, 2020))
    print(delete_year(ankara_data, 2020))
    
    #print(monthly_averages(istanbul_data, 2017))
    print(monthly_averages(ankara_data, 2017))
   



################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()
