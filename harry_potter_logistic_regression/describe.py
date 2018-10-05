#!/usr/bin/env python

import os
import sys
import numpy as np
import matplotlib as mpl
#from . import utils
#import utils
#import fmtp
from tabulate import tabulate


def describe(filepath = '../data/dataset_train.csv', number_of_columns=15):
    # filename = get_filename()
    if get_filepath() is not None:
        filepath = get_filepath()
    # filepath = '../data/dataset_train.csv'
    # filepath = filepath.join(filename)
    with open(filepath, 'r') as f:
      header = f.readline()
      h=header.split(',')
      h.insert(0, '')

    data = np.genfromtxt(filepath, delimiter=',', skip_header=1)
    # data = data[:,1:]
    # print('\t\t' + '\t'.join([i for i in header.split(',') if i!='Index']) + '\n')
    
    count = list(np.count_nonzero(~np.isnan(data), axis=0))
    count.insert(0, 'Count')
    mean = list(np.mean(~np.isnan(data), axis=0))
    mean.insert(0, 'Mean')
    std = list(np.std(~np.isnan(data), axis=0))
    std.insert(0, 'Standard Dev.')
    min = list(np.min(~np.isnan(data), axis=0))
    min.insert(0, 'Min.')
    perc_25 = list(np.percentile(~np.isnan(data), 0.25, axis=0))
    perc_25.insert(0, '25%')
    perc_50 = list(np.percentile(~np.isnan(data), 0.5, axis=0))
    perc_50.insert(0, '50%')
    perc_75 = list(np.percentile(~np.isnan(data), 0.75, axis=0))
    perc_75.insert(0, '75%')
    max = list(np.max(~np.isnan(data), axis=0))
    max.insert(0, 'Max')

    # print('Count\t' + '\t'.join(np.array2string(count)))
    if get_number_of_columns() is not None:
        number_of_columns = int(get_number_of_columns())
    h = h[:number_of_columns]
    count = count[:number_of_columns]
    mean = mean[:number_of_columns]
    std = std[:number_of_columns]
    min = min[:number_of_columns]
    perc_25 = perc_25[:number_of_columns]
    perc_50 = perc_50[:number_of_columns]
    perc_75 = perc_75[:number_of_columns]
    max = max[:number_of_columns]

    print(tabulate([count, mean, std, min, perc_25, perc_50, perc_75, max], headers=h))

    #

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
    if sys.argv[1] is not None:
        filepath = sys.argv[1]
    # dirname = os.path.dirname('/Users/vmalesev/Desktop/Ecole42_logistic_regression/data')
    # filepath = os.path.join(dirname, filepath)

    return filepath

def get_number_of_columns():
    if sys.argv[2] is not None:
        number_of_columns = sys.argv[2]
    return number_of_columns


#if __name__ == "__main__":
describe()
