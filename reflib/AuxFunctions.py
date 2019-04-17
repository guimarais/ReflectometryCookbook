from scipy.constants import codata
import numpy as np

def n2f(n):
    """Converts a density in m^-3 to the corresponding O-mode frequency in Hz
    
    Parameters
    -----------
    n : float
        The input density in m^-3
    
    Returns
    -----------
    f : float
        The corresponding frequency in Hertz
    """
    k = 4.0 * np.pi**2 * codata.value('electron mass') * codata.value('electric constant') / codata.value('elementary charge')**2
    f = np.sqrt(n/k)
    return f


def f2n(f):
    """Converts a frequency in Hertz to the corresponding O-mode density in m^-3
    
    Parameters
    -----------
    f : float
        The input frequency in Hertz
    
    Returns
    -----------
    n : float
        The corresponding density in m^-3
    """
    k = 4.0 * np.pi**2 * codata.value('electron mass') * codata.value('electric constant') / codata.value('elementary charge')**2
    n = k * f**2
    return n

def b2f(b):
    """Converts a magnetic field in Tesla to the corresponding cyclotronic frequency in Hz
    
    Parameters
    -----------
    b : float
        The input magnetic field in Tesla
    
    Returns
    -----------
    f : float
        The corresponding cyclotronic frequency in Hertz
    """
    k =  codata.value('elementary charge') / (2.0 * np.pi * codata.value('electron mass'))
    f = k*b
    return f

def f2b(f):
    """Converts a cyclotronic frequency in Hz into its corresponding Magnetic field
    
    Parameters
    -----------
    f : float
        The input frequency in Hz
    
    Returns
    -----------
    b : float
        The corresponding magnetic field in Tesla
    """
    k = 2.0 * np.pi * codata.value('electron mass') / codata.value('elementary charge')
    b = k*f
    return b