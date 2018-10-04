#!/usr/bin/env python

import os
import sys
import numpy as np
import matplotlib as mpl
#from . import utils
import utils
#import fmtp
from tabulate import tabulate


def describe():
    filepath = get_filepath()
    data = np.genfromtxt(filepath, delimiter=',', skip_header=1)
    count = np.count_nonzero(data, axis=1)
    mean = np.mean(data, axis=1)
    std = np.std(data, axis=1)
    min = np.min(data, axis=1)
    perc_25 = np.percentile(data, 0.25, axis=1)
    perc_50 = np.percentile(data, 0.5, axis=1)
    perc_75 = np.percentile(data, 0.75, axis=1)
    max = np.max(data, axis=1)

    print('Summary:')
    display_data = [[utils.fmtp(count), utils.fmtp(mean), utils.fmtp(std),
                     utils.fmtp(min), utils.fmtp(perc_25),
                     utils.fmtp(perc_50), utils.fmtp(perc_75),
                     utils.fmtp(max)]]
    print(tabulate(display_data, headers=['Count', 'Mean', 'Standard Dev.',
                                          'Min', '25% Perc.',
                                          '50% Perc.', '75% Perc.',
                                          'Max']))


def get_filepath():
    filepath = sys.argv[1]
#    dirname = os.path.dirname('/Users/vmalesev/Desktop/Ecole42_logistic_regression/data')
#    filepath = os.path.join(dirname, filepath)

    return filepath



#if __name__ == "__main__":
describe()