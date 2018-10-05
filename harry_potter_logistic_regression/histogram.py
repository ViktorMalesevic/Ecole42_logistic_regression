#!/usr/bin/env python

import utils as ul  # our own module
import matplotlib.pyplot as plt


def histogram():
    data = ul.create_dataframe()
    plt.hist(data)


histogram()
