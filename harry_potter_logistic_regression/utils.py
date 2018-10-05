#!/usr/bin/env python

import sys
import numpy as np


def create_dataframe(filepath = '../data/dataset_train.csv'):
    if get_filepath() is not None:
        filepath = get_filepath()
    data = np.genfromtxt(filepath, delimiter=',')
    return data


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
