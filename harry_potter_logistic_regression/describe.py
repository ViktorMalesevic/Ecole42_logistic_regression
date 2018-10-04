#!/usr/bin/env python

import os
import sys
import numpy as np
import matplotlib as mpl
#from . import utils
#import utils
#import fmtp
from tabulate import tabulate


def describe():
    #filepath = get_filepath()
    filepath = '../data/dataset_train.csv'
    with open(filepath, 'r') as f:
      header = f.readline()
      h=header.split(',')
      h.insert(0, '')

    data = np.genfromtxt(filepath, delimiter=',', skip_header=1)
    #data = data[:,1:]
    #print('\t\t' + '\t'.join([i for i in header.split(',') if i!='Index']) + '\n')
    
    count = list(np.count_nonzero(~np.isnan(data), axis=0))
    count.insert(0, 'Count')
    #print('Count\t' + '\t'.join(np.array2string(count)))
    h=h[:10]
    count=count[:10]
    print(tabulate([count], headers=h))

    # mean = np.mean(data, axis=1)
    # std = np.std(data, axis=1)
    # min = np.min(data, axis=1)
    # perc_25 = np.percentile(data, 0.25, axis=1)
    # perc_50 = np.percentile(data, 0.5, axis=1)
    # perc_75 = np.percentile(data, 0.75, axis=1)
    # max = np.max(data, axis=1)

    # print('Summary:')
    # display_data = [[utils.fmtp(count), utils.fmtp(mean), utils.fmtp(std),
    #                  utils.fmtp(min), utils.fmtp(perc_25),
    #                  utils.fmtp(perc_50), utils.fmtp(perc_75),
    #                  utils.fmtp(max)]]
    # print(tabulate(display_data, headers=['Count', 'Mean', 'Standard Dev.',
    #                                       'Min', '25% Perc.',
    #                                       '50% Perc.', '75% Perc.',
    #                                       'Max']))


def get_filepath():
    filepath = sys.argv[1]
#    dirname = os.path.dirname('/Users/vmalesev/Desktop/Ecole42_logistic_regression/data')
#    filepath = os.path.join(dirname, filepath)

    return filepath



#if __name__ == "__main__":
describe()