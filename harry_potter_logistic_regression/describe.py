#!/usr/bin/env python

import os
import sys
import numpy as np
import matplotlib as mpl


data = np.genfromtxt(input('Please provide the file path'), delimiter=',', skip_header=1)

# Script option

count = np.count_nonzero(data, axis=1)
mean = np.mean(data, axis=1)
std = np.std(data, axis=1)
min = np.min(data, axis=1)
perc_25 = np.percentile(data, 0.25, axis=1)
perc_50 = np.percentile(data, 0.5, axis=1)
perc_75 = np.percentile(data, 0.75, axis=1)
max = np.max(data, axis=1)


# Class option
class Describe(object):

    def __init__(self, data):
        super(Describe, self).__init__()
        self.data = data

    def calculate






if __name__=="__main__":
    main()
