# welcome on branch

import numpy as np

np.random.seed(1)

def growth_rate(x, steps=1):
  """ calculates first differences"""
  return x[steps:]-x[:-steps]

def create_DGP(N, T, alpha, var_eps):
  """ Function that takes all parameters and returns a simulated dataset [NxT]"""
  Y=np.random.rand(N, T)
  for i in range(N):
    Y[i, 0]=0
    theta = np.random.uniform(1, alpha, 1)
    for t in range(1, T):
      epsilon = np.random.normal(0, sqrt(var_eps), 1)
      Y[i, t]=theta+Y[i, t-1]+epsilon

  # unit tests for simulating DGP
  assert np.mean(Y, axis = 0)[0] == 0 # start time series 0 at t=0
  return Y