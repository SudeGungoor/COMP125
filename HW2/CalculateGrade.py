
def calculate_grade(lab_scores, hw_scores, mt_scores, final_exam_score):
    
    if len(lab_scores)!=6 or len(hw_scores)!=6 or len(mt_scores)!=6:
        return -1
    for i in range(6):
        if lab_scores[i]<0 or hw_scores[i]<0 or mt_scores[i]<0 or final_exam_score<0 :
          return -2
    else:
        total = 0
        lab_scores.sort()
        lab_scores.remove(lab_scores[0])
        lab_scores.remove(lab_scores[0])
        lab = 0.1 *(lab_scores[0]+lab_scores[1]+lab_scores[2]+lab_scores[3])/4
        hw_scores.sort()
        hw_scores.remove(hw_scores[0])
        hw_scores.remove(hw_scores[0])
        hw = 0.2 * (hw_scores[0]+hw_scores[1]+hw_scores[2]+hw_scores[3])/4
        mt_scores.sort()
        mt_scores.remove(mt_scores[0])
        mt_scores.remove(mt_scores[0])
        mt = 0.4 * (mt_scores[0]+mt_scores[1]+mt_scores[2]+mt_scores[3])/4
        final = final_exam_score * 0.3
        total = lab + hw + mt + final
        return total

        

def main():
    '''
    You can test your calculate_grade implementation using the function calls here.
    These function calls are here only to help you test your function.
    What matters is whether your calculate_grade function is correct.
    '''
    
    labs = [100, 85.5, 90, 90, 100, 78]
    hws = [83.75, 82.0, 100, 100, 100, 100]
    mts = [62, 91, 93, 59.0, 98.5, 80]
    final_score = 78.0
    
    print(calculate_grade(labs, hws, mts, final_score))
    

    
################################################################ 
'''
DO NOT EDIT BELOW THIS LINE
'''
if __name__ == '__main__':
    main()