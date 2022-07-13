def read_iris(filename):
    file = open('iris_data.csv','r')   
    final = []
    for i in file: 
        x = []
        i = i.strip()
        a = i.split(",")
       
        for i2 in a:
            if '.' in i2 or i2.isdigit() == True :
                x.append(float(i2))
            else:
                x.append(i2)
        final.append(x)
    del final[0]    
    file.close()
    return final

def avg_versicolor(lst):
    count = 0 
    total = 0
    for j in len(lst):
        
        for row in lst:
            if row[j] == row[0]:
                total += float(row[0])
                
            elif row[j]==row[2]:
                total += float(row[2])
                
                count += 1     
            avg = total / count

    return avg
    
    
    
         
            
    return total # change me



def main():
    """
    The code given here is for you test your functions. When submitting, 
    make sure the code you leave under main() does not cause a syntax error.
    """
    
    my_list = read_iris('iris_data.csv')
    print(my_list)
    avg = avg_versicolor(my_list)
    print(avg)
    
    

################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()
