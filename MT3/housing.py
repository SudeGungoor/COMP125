def read_data(filename):
    
    list1=[]
    list2=[]
    file = open(filename,'r')
    for line in file:
        list2=[]
        line=line.rstrip()
        list2=line.split(",")
        if list2 != ['Price', 'Type', 'Living_space', 'Bedrooms', 'Bathrooms', 'Year_built', 'Year_renovated']:
            for i in range(0,7):
               if i==2:
                   list2[2]=float(list2[2])
               if i>2 or i==0:
                   list2[i]=int(list2[i])
            list1.append(list2)
    file.close()
    return list1

def filter_data(lst, bed, bath, year):
    
    
    list1=[]
    for i in lst:
        count=0
        for a in range(0,6):
            
            if a==3:
                item=int(i[a])
                if item>bed:
                    count = count+1
            if a==4:
                item=int(i[a])
                if item>bath:
                    count = count+1   
            if a==5:
                item=int(i[a])
                if item>year:
                    count = count+1
        if count == 3:
            list1.append(i)
    return list1 




def filter_price(lst, min_price, max_price):
    
    
    list1=[]
    for i in lst:
        for a in range(0,6):      
            if a==0:
                item=int(i[a])
                if item>min_price and item<max_price:
                    list1.append(i)
    return len(list1) 


def report(lst, year):
    
    
    string=""
    file=open("riskreport.txt", "w")
    for i in lst:
        for a in range(0,7):
            if a==5:
                item=int(i[a])
                string=""
                if item<year:
                    string=i[1]+","+str(i[5])+","+str(i[6])+"\n"
                    file.write(string)
    file.close()               
    
    

def main():
    """
    The code given here is for you test your functions. You can modify
    it to perform more tests. When submitting, make sure the code you
    leave under main() does not cause a syntax error.
    """
    
    # Part 1
    filename = 'HousingData.csv'
    data = read_data(filename)
    
    # Part 2
    filtered_data = filter_data(data, 2,2, 1900)
    print(filtered_data)
    
    # Part 3
    filtered_price=filter_price(data, 40000, 120000)
    print(filtered_price)
    
    # Part 4
    report(data, 1900)
    
    
################################################################ 

'''
DO NOT EDIT BELOW THIS LINE
'''
if __name__ == '__main__':
    main()
    
    