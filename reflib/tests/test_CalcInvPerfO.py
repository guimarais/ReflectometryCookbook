import numpy as np
from reflib import CalcInvPerfO

def test_CalcInvPerfO():
    assert np.round(CalcInvPerfO([1,1], [1,1], vacd=1)[0][1])==4684258
    assert np.shape(CalcInvPerfO([1,1], [1,1], vacd=1))==(4,34)
