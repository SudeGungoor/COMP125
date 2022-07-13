def read_data(filename):

    list1=[]
    list2=[]
    file = open(filename,'r')
    for line in file:
        list2=[]
        line=line.rstrip()
        list2=line.split("-")
        if line != "Sex-Age-Hypertension-Heart Disease-Residence Type-Glucose-Smoking Status":
            for i in range(0,7):
               if i==5:
                   list2[5]=float(list2[5])
               if i==1:
                   list2[1]=int(list2[1])
            list1.append(list2)
    file.close()
    return list1


def stats_glucose(lst,smoking_stat):
    
    
    avg_F=0
    avg_M=0
    Mcount=0
    Fcount=0
    for i in lst:
        for a in range(0,7):
            if a==6:
                item=str(i[6])
                if item==smoking_stat:
                    item2=str(i[0])
                    if item2=='M':
                        Mcount=Mcount+1
                        avg_M=avg_M+float(i[5])
                    if item2=='F':
                        Fcount=Fcount+1
                        avg_F=avg_F+float(i[5])
    avg_F=avg_F/Fcount
    avg_M=avg_M/Mcount
    return [('F', avg_F), ('M', avg_M)]#CHANGE ME


def calculate_ratio(lst,age):
    
    
    Rcount=0
    Ucount=0
    for i in lst:
        for a in range(0,7):
            if a==1:
                item=int(i[1])
                if item>age:
                    item2=str(i[4])
                    if item2=='Rural':
                        Rcount=Rcount+1

                    if item2=='Urban':
                        Ucount=Ucount+1
 
    return Rcount/Ucount   
            
def main():
    
    #Part A:
    my_list= read_data('stroke.txt')
    print(my_list)
    
    #Part B:
    print(stats_glucose(my_list,'never smoked'))
    
    #Part C:
    print(calculate_ratio(my_list,65))
    
    
    
################################################################ 

'''
DO NOT EDIT BELOW THIS LINE
'''
if __name__ == '__main__':
    main()
    
    