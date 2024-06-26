'''
file name: 'fitting.py'
repository: 'ILP-Land-Usage'
@author: evanh
._.

Requirements:
    - 


'''



import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcol
from matplotlib.colors import LinearSegmentedColormap

import seaborn as sns
import seaborn.objects as so

import scipy
from scipy.optimize import LinearConstraint
from scipy.optimize import minimize

from collections import Counter

import math
import random
import sys
import time



'''
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
'''



def main():
    from sklearn.datasets import make_friedman2
    X, y = make_friedman2(n_samples=500, noise=0, random_state=0)
    kernel = DotProduct() + WhiteKernel()
    gpr = GaussianProcessRegressor(kernel=kernel,
            random_state=0).fit(X, y)
    gpr.score(X, y)
    gpr.predict(X[:2,:], return_std=True)


if __name__ == "__main__":
    main()



