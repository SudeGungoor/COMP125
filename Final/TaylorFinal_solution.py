import numpy as np
import matplotlib.pyplot as plt


def factorial(n):
    res = 1.0
    for i in range(1, n+1):
        res = res * i
    return res


def taylor_sin(x, terms):
    s = 0
    for i in range(0, terms):
        term = x**(2*i+1) / factorial(2*i+1)
        if i % 2 != 0:
            # odd, then subtract
            s = s - term            
        else:
            # even, then add
            s = s + term
    return s


def calc_err_sin(x, start_term, end_term):
    errors = []
    for i in range(start_term, end_term+1):
        my_result = taylor_sin(x, i)
        act_result = np.sin(x)
        errors.append(abs(my_result - act_result))
    return errors



def graph_errors(x_vals, start_term, end_term):    
    graph_x = list(range(start_term, end_term+1))
    for x in x_vals:
        y_i = calc_err_sin(x, start_term, end_term)
        plt.plot(graph_x, y_i, label='x = {}'.format(x))
    plt.legend()
    plt.xlabel("Number of Terms")
    plt.ylabel("Error")
    plt.title("Approximating Sinus with Taylor Series")
    plt.show()
    


def main():
    """
    You can test your implementations using the function calls here.
    """
    # Part A
    print(taylor_sin(10, 2))
    print(taylor_sin(10, 10))
    print(taylor_sin(10, 15))
    print(taylor_sin(10, 20))
    
    # Part B
    errors = calc_err_sin(15, 10, 30)
    print(errors)
    
    # Part C
    graph_errors([9, 10, 11], 6, 15)
    

    
################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()