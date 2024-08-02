
import scipy as sp
from scipy.optimize import LinearConstraint
from scipy.optimize import minimize

import fitting


def f(x):
    import numpy as np

    #offset = np.random.normal(0, 10, 4)
    #parameters = np.array([x1,x2,x3,x4]) + offset
    
    c1, c2, c3, c4, c5 = CONSTANTS
    x1, x2, x3, x4 = x
    return -1*MODEL.predict(np.array([c1, c2, c3, c4, c5, x1, x2, x3, x4]).reshape(1,-1))



def main(feature_constants):
    global CONSTANTS
    CONSTANTS = feature_constants

    CONSTANTS[3] *=100
    CONSTANTS[2] *=10
    CONSTANTS[0] *=100
    CONSTANTS.append(CONSTANTS[4]- CONSTANTS[5])
    CONSTANTS.pop(5)
    CONSTANTS.pop(4)
    CONSTANTS[0] = int(CONSTANTS[0])
    CONSTANTS[2] = int(CONSTANTS[2])
    print(CONSTANTS)

    global MODEL
    MODEL = fitting.main()


    buildings_max = CONSTANTS[1]/0.05

    #cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2},
    #    {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
    #    {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
    #    {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})
    cons = ()
        
    bnds = ((50, buildings_max), (50, buildings_max), (50, buildings_max), (50, buildings_max))

    #minimize(f, [15000, 5000, 5000, 5000], method='BFGS', options={'gtol': 1e-1, 'disp': True})
    return minimize(f, [100, 500, 500, 500], bounds=bnds, constraints=cons, method='SLSQP', options={"disp":True})


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])


