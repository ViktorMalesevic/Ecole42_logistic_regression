#!/usr/bin/env python

import os
import sys
import numpy as np
import matplotlib as mpl
from . import utils
from .utils import fmtp
from tabulate import tabulate


# Class option
class Describe(object):

    def __init__(self, filepath):
        super(Describe, self).__init__()
        self.filepath = filepath
        self._read_data(self.filepath)
        self._calculate(self.data)

    def _read_data(self, filepath):
        self.data = np.genfromtxt(self.filepath, delimiter=',', skip_header=1)

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

        count = np.count_nonzero(self.data, axis=1)
        mean = np.mean(self.data, axis=1)
        std = np.std(self.data, axis=1)
        min = np.min(self.data, axis=1)
        perc_25 = np.percentile(self.data, 0.25, axis=1)
        perc_50 = np.percentile(self.data, 0.5, axis=1)
        perc_75 = np.percentile(self.data, 0.75, axis=1)
        max = np.max(self.data, axis=1)

        self.count = count
        self.mean = mean
        self.std = std
        self.min = min
        self.perc_25 = perc_25
        self.perc_50 = perc_50
        self.perc_75 = perc_75
        self.max = max

    def display(self):
        print('Summary:')
        display_data = [[fmtp(self.count), fmtp(self.mean), fmtp(self.std),
                         fmtp(self.min), fmtp(self.perc_25),
                         fmtp(self.perc_50), fmtp(self.perc_75),
                         fmtp(self.max)]]
        print(tabulate(display_data, headers=['Count', 'Mean', 'Standard Dev.',
                                              'Min', '25% Perc.',
                                              '50% Perc.', '75% Perc.',
                                              'Max']))


if __name__ == "__main__":
    filepath = sys.argv[1]
#    main()
    Describe(filepath)
