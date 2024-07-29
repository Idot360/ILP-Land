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



def main(params):
    import pandas as pd
    import numpy as np

    import fitting
    import optimization


    features = ["Population","Land size","Working hours","Corruption","Environment","Income","Cost of living","N recreational buildings","N office buildings","N essential buildings","N residential buildings"]

    model = fitting.main()





if __name__ == "__main__":
    import sys
    main(sys.argv[1:])