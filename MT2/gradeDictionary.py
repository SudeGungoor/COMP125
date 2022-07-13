def calculate_avg(d):
    toplam = 0
    toplam2 = 0
    for i in range(len(d)):
        liste = list(d.keys())
        value = d.get(liste[i])
        value2 =list(value.values())[0]
        toplam += value2
        value3 =list(value.values())[1]
        toplam2 += value3  
    return toplam / len(d) , toplam2 / len(d)
def higher_grade(d):
    x = []
    names = list(d.keys())
    for name in names:
        #print(name)
        v = d.get(name)
        if list(v.values())[0] != list(v.values())[1]:
            #print(max(v.values()))
            index_ = list(v.values()).index(max(v.values()))
            a = (str(name) , str(list(v.keys())[index_]))
            x.append(a)
        elif list(v.values())[0] == list(v.values())[1]:
            #print(max(v.values()))
            #index_ = list(v.values()).index(max(v.values()))
            a = (str(name) , -1)
            x.append(a)
    return x
    
    
def main():
    
    test_d = {'Maria': {'math': 67, 'science': 45},
   	         'John': {'math': 88, 'science': 90}, 
	        'Sarah': {'math': 65, 'science': 90},
    	       'Albert': {'math': 74, 'science': 60},
   	         'Bob': {'math': 100, 'science': 65}}
   
    av1,av2 = calculate_avg(test_d)
    print(av1,av2)

    result = higher_grade(test_d)
    print(result)   
    
################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()


