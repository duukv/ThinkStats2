"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import os
import sys
from operator import itemgetter

os.chdir(".\code")
import first

import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    freq_dict = {v: k for k, v in hist.Items()}
    freq_list = [v for k, v in hist.Items()]
    highest = sorted(freq_list, reverse=True)[0]
    return freq_dict[highest]


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    modes = [(k, v) for k, v in hist.Items()]
    modes.sort(key=lambda x: x[1], reverse=True)
    return modes


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # # test Mode
    Mode(hist)
    mode = Mode(hist)
    print("Mode of preg length", mode)
    assert mode == 39, mode

    # test AllModes
    modes = AllModes(hist)
    assert modes[0][1] == 4693, modes[0][1]

    for value, freq in modes[:5]:
        print(value, freq)

    print("mean totalwgt_lb live births ", live["totalwgt_lb"].mean())
    print("mean totalwgt_lb firsts births ", firsts["totalwgt_lb"].mean())
    print("mean totalwgt_lb others births ", others["totalwgt_lb"].mean())
    print(
        "cohens effectsize ",
        thinkstats2.CohenEffectSize(firsts["totalwgt_lb"], others["totalwgt_lb"]),
    )

    print("%s: All tests passed." % script)


if __name__ == "__main__":
    main(*sys.argv)
