import numpy as np
from reflib import SimulDensPerf

def test_SimulDensPerf():
    assert np.shape(SimulDensPerf())==(2,100)
    assert max(SimulDensPerf(dens0=0.0)[1][:])==0.0
