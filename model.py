import numpy as np
import statsmodels.api as sm
import statsmodels.stats as stats
def CRDW(Y, i, tao):
    """ find cointegrating countries """
    N, T = Y.shape
    JH = Y[i][1:-1]
    for j in range(N):
        if j!=i:
            y = Y[i]
            x = Y[j]
            x = sm.add_constant(x)
            model = sm.OLS(y, x)
            results = model.fit()
            CRDW_j = stats.stattools.durbin_watson(results.resid)
            if CRDW_j > tao:
                JH = np.vstack((JH, Y[j][1:-1]))
    assert JH.shape[0]>0

    return JH