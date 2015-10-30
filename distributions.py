# -*- coding: utf-8 -*-

import scipy as sp
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

#--------------- Creating Distributions  ------------------------------------ #

s = sp.randn(100) # Hundred random numbers from a standard Gaussian
print len(s)
print("Mean : {0:8.6f}".format(s.mean()))   # using class function
print("Minimum : {0:8.6f}".format(s.min()))
print("Maximum : {0:8.6f}".format(s.max()))
print("Variance : {0:8.6f}".format(s.var()))
print("Std. deviation : {0:8.6f}".format(s.std()))
print("Mean : {0:8.6f}".format(sp.mean(s))) # using scipy mean function 

# Describe function returns these quantities in single shot
from scipy import stats
n, min_max, mean, var, skew, kurt = stats.describe(s)


#--------------- Gaussians and Binomials ------------------------------------ #
n = stats.norm(loc=3.5, scale=2.0)      # define a gaussian distribution
x = n.rvs()                             # sample a gaussian random variable
stats.norm.rvs(loc=3.5, scale=2.0)      # single line sampler from normal dist
stats.norm.cdf(0.2, loc=0.0, scale=1.0) # CDF

stats.norm.pdf(0, loc=0.0, scale=1.0)   # PDF of a specified Gaussian
stats.norm.pdf([-0.1, 0.0, 0.1], loc=0.0, scale=1.0) # multiple queries

tries = range(11)                       # 0 to 10
print(stats.binom.pmf(tries, 10, 0.5))  # Binomial PMF p=0.5, n=10



