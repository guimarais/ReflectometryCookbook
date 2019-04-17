import numpy as np
from reflib.AuxFunctions import f2n

def test_f2n():
    np.round(f2n(29e9)/1e18)==10
    np.floor(f2n(69e9)/1e17)==590
