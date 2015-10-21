# read simple two column file
# 1 3 
# 2 4
# 8 9

import numpy as np
import matplotlib.pyplot as plt

with open("lda-c/ap/likelihood.dat") as f:
    data = f.read()

data = data.split('\n')