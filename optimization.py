
def f(x1, x2, x3, x4):
    #offset = np.random.normal(0, 10, 4)
    #parameters = np.array([x1,x2,x3,x4]) + offset
    
    c1, c2, c3, c4, c5, c6, c7 = CONSTANTS
    return MODEL.predict()



def main(feature_constants):
    import scipy as sp
    from scipy.optimize import LinearConstraint
    from scipy.optimize import minimize

    import fitting

    global CONSTANTS
    CONSTANTS = feature_constants

    global MODEL
    MODEL = fitting.main()


    buildings_max = CONSTANTS[1]/0.005

    #cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2},
    #    {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
    #    {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
    #    {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})
    cons = ()
    
    bnds = ((1, buildings_max), (1, buildings_max), (1, buildings_max), (1, buildings_max))

    return minimize(f, [5, 5, 5, 5], bounds=bnds, constraints=cons)


if __name__ == "__main__":
    import sys
    #main(sys.argv[1:])
    main([2.7,223,31.6,2,6,96000,83600,5000,3500,1430,1600])



