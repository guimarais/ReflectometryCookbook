import numpy as np

def SimulDensPerf(dens0 = 6e19, Rmid=1.65, R0=2.22, Rant=2.32, m=13, n=4, npts=100):
    """Makes a LFS density profile in real space
    
    Parameters
    -----------
    dens0 : float
            Density at Rmid point
    Rmid : float
           Mid-point of the plasma column (core):
    R0 : float
         Last plasma point
    Rant : float
           Radial location of antennas
    m : int
        Geometric parameter for density profile
    n : int 
        Geometric parameter for density profile
    npts : int
           Number of points for the profile (going from Rmid to Rant)
    
    Returns
    -----------
    r : array
        Profile radius
    dens : array
           Profile density
    """
    #Declare the radii
    r = np.linspace(Rmid, Rant, npts)
    #Declare the density
    dens = np.zeros_like(r)
    #n[rmask] = dens0*( 1.0 - ((r[rmask]-Rmid)/(R0-Rmid))**m)**n
    dens = dens0*( 1.0 - ((r-Rmid)/(R0-Rmid))**m)**n
    rmask = r>R0
    dens[rmask] = 0.0
    return r, dens