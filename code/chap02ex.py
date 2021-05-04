"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter
from typing import OrderedDict

import first
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    mode = max((freq, val) for val, freq in hist.Items())[1]
    
    return mode


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    modes = sorted(hist.Items(), key=itemgetter(1) ,reverse=True)

    return modes

def WeightDifference(live, firsts, others):
    """
    Using the variable "totalwgt_lb", investigate whether first
    babies are lighter or heavier than others.  Compute Cohen's d
    to quantify the difference between the groups.  How does it
    compare to the difference in pregnancy length?
    """
    
    live.__name__ = 'live'
    firsts.__name__ = 'firsts'
    others.__name__ = 'others'

    mean_d = {}
    var_d = {}
    totalwgt_serie_d = {}

    for df in live, firsts, others:
        print(f"The Mean totalwgt of {df.__name__} is {df.totalwgt_lb.mean()}")
        print(f"The totalwgt var of {df.__name__} is {df.totalwgt_lb.var()}\n")
        mean_d[df.__name__] = df.totalwgt_lb.mean()
        var_d[df.__name__] = df.totalwgt_lb.var()     
        totalwgt_serie_d[df.__name__] = df.totalwgt_lb

    d = thinkstats2.CohenEffectSize(totalwgt_serie_d['firsts'], totalwgt_serie_d['others'])

    print(f"Difference in mean = {mean_d['firsts']-mean_d['others']}")
    print(f"Difference in mean in % = {(mean_d['firsts']-mean_d['others'])/mean_d['live']*100}")
    print(f"Cohen's d = {d}")
    return d


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test
    WeightDifference(live, firsts, others)
    assert WeightDifference(live, firsts, others) == -0.088672927072602

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert mode == 39, mode

    # test AllModes
    modes = AllModes(hist)
    assert modes[0][1] == 4693, modes[0][1]

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
