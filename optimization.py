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

import scipy as sp
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



def f(x1, x2, x3, x4):
    offset = np.random.normal(0, 10, 4)
    parameters = np.array([x1,x2,x3,x4]) + offset
    return parameters.sum()



def main():
    sp
    return 0


if __name__ == "__main__":
    main()



