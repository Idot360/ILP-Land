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

import sklearn as skl
from sklearn.gaussian_process import GaussianProcessRegressor # example algorithm
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import pairwise_distances_argmin_min

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
    print(X.shape)
    print(y.shape)
    kernel = DotProduct() + WhiteKernel()
    gpr = GaussianProcessRegressor(kernel=kernel,
            random_state=0).fit(X, y)
    gpr.score(X, y)
    gpr.predict(X[:2,:], return_std=True)


if __name__ == "__main__":
    main()



