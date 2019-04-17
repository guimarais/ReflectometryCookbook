import numpy as np
from reflib.AuxFunctions import n2f

def test_n2f():
    assert np.round(n2f(1.12e19)/1e8)==300
    assert np.round(n2f(6.e19)/1e8)==695
