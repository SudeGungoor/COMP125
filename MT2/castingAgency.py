def casting_record(rec):
    total = []
    for i in rec :
        for j in i:
            j = i.split('-')
            k = ["0","1","2"]
            for l in range(len(j)):
                if j[l].isalpha() and j[l].islower() and j[l] == str(j[l]) :
                    k[0] = j[l].capitalize()
                elif j[l].isdigit():
                    k[2] = j[l] 
                else:
                    k[1] = j[l]
        total.append(k)         
    return total

def main():
    
    test_list = ['severus-SNAPE-2343',
                 'POTTER-5674-harry',
                 'WEASLEY-4389-ron',
                 '2365-draco-MALFOY',
                 'hermione-1478-GRANGER']
    
    result = casting_record(test_list)
    print(result)

################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()