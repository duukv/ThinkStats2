#%%
import os

from matplotlib.pyplot import ylabel
import thinkplot
import thinkstats2
import numpy as np
import sys
import nsfg
#%%

def PmfMean(pmf):
    """Calculate the mean of a PMF

    Returns:
        float
    """
    l = [x*p for x, p in pmf.Items()]
    mean = sum(l)
    return mean
#%%
def PmfVar(pmf):
    """Calculate the variance of a PMF

    Returns:
        float
    """
    l = [p*(x-PmfMean(pmf))**2 for x, p in pmf.Items()]
    var = sum(l)
    return var
#%%
def MeanPairDifferences():
    """Calculate mean difference between first born and other for the same mother

    """
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    live = live[live.prglngth >= 37]
    preg_map = nsfg.MakePregMap(live)

    diffs = []
    for _, indices in preg_map.items():
        if len(indices) > 1:
            first = indices[0]
            rest = indices[1:]
            
            for x in rest:
                diff = live.loc[first].prglngth - live.loc[x].prglngth
                diffs.append(diff)
    
    mean = thinkstats2.Mean(diffs)
    print("mean difference between pairs: ", mean)

    pmf = thinkstats2.Pmf(diffs)
    thinkplot.Hist(pmf, align='center')
    thinkplot.Show(xlabel='Difference in weeks',ylabel='PMF')
# %%

def main():
    os.chdir("code")
    x = np.random.randint(10,size=10)
    pmf = thinkstats2.Pmf(x)

    print("thinkstats2.Pmf.Mean -->" ,pmf.Mean())
    print("PmfMean(pmf) -->", PmfMean(pmf))
    print("thinkstats2.Pmf.Var -->" ,pmf.Var())
    print("PmfVar(pmf) -->", PmfVar(pmf))

    MeanPairDifferences()

    print(f"{sys.argv[0]} all tests passed")

if __name__ == '__main__':
    main()
