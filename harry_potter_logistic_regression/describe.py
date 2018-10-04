#!/usr/bin/env python

import os
import sys
import numpy as np
import matplotlib as mpl


# Class option
class Describe(object):

    def __init__(self, filepath):
        super(Describe, self).__init__()
        self.filepath = filepath
        self._read_data(self.filepath)
        self._calculate(self.data)

    def _read_data(self, filepath):
        self.data = np.genfromtxt(filepath, delimiter=',', skip_header=1)

    def _calculate(self, data):
        # default values
        self.count = np.nan
        self.mean = np.nan
        self.std = np.nan
        self.min = np.nan
        self.perc_25 = np.nan
        self.perc_50 = np.nan
        self.perc_75 = np.nan
        self.max = np.nan

        count = np.count_nonzero(data, axis=1)
        mean = np.mean(data, axis=1)
        std = np.std(data, axis=1)
        min = np.min(data, axis=1)
        perc_25 = np.percentile(data, 0.25, axis=1)
        perc_50 = np.percentile(data, 0.5, axis=1)
        perc_75 = np.percentile(data, 0.75, axis=1)
        max = np.max(data, axis=1)

        self.count = count
        self.mean = mean
        self.std = std
        self.min = min
        self.perc_25 = perc_25
        self.perc_50 = perc_50
        self.perc_75 = perc_75
        self.max = max


if __name__=="__main__":
    filepath = sys.argv[1]
    main()
    filepath.Describe()
