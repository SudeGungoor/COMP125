
def calculate_cos(vectors): 
    x = []
    for i in vectors:
        result = 0
        for j in vectors:
            if i != j:
                a , b = i
                c , d = j
                n = (a * c) + (b * d)
                u = (a**2 + b**2)**0.5  
                v = (c**2 + d**2)**0.5
                result = n / (u * v)
                x.append(result) 
    result2 = min(x)
    for i in vectors:
        result = 0
        for j in vectors:
            if i != j:
                a , b = i
                c , d = j
                n = (a * c) + (b * d)
                u = (a**2 + b**2)**0.5  
                v = (c**2 + d**2)**0.5
                result = n / (u * v)
                if result == result2:
                    return i , j
def main():
    
    test = [(7,1), (5,5), (-4,0)]
    test = [(-4,0), (4,0), (3,4)]
    test = [(3,2), (-2,7), (6,1), (1,3)]
    
    tup1, tup2 = calculate_cos(test)
    print(tup1,tup2)
    
################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()
    
    