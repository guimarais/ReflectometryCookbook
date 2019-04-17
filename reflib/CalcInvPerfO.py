import numpy as np
import scipy.constants as konst
from AuxFunctions import *

def CalcInvPerfO(fpro, gdel, vacd=0.0, initpts=32):
    """Inverts an O-mode groupd delay into a density profile.
    Group delay is not initialized
    
    Parameters
    ------------
    fpro: array
          Probing frequencies
    gdel: array
          Group delays. Must be the same size as "fpro"
    vacd: float
          Vaccuum distance to the antenna: where the plasma is believed to start.
    initpts: int
             How many points to be used in the initialization

    Returns
    ------------
    rad: array
         Radius
    dens: array
          Density
    fpro: array
          The actual probing frequency used to calculate the density profile
    gdel: array
          The actual group delay used to calculate the density profile
    """

    k3 = konst.c/(2*np.pi*np.pi)

    #Initialization points
    init0_f = 0.0
    vac_gdel = 2.0 * vacd / konst.c
    init0_g = vac_gdel    
    
    init1_f = fpro[0]
    init1_g = gdel[0]

    #Automatically initializes GD, if Fprobe starts at zero this does nothing
    initf = np.linspace(init0_f, init1_f, num=initpts, endpoint=False)
    initg = np.linspace(init0_g, init1_g, num=initpts, endpoint=False)

    fpro = np.concatenate((initf, fpro))
    gdel = np.concatenate((initg, gdel))

    #Converts the density
    dens = f2n(fpro)
    
    #Gets the integral done
    summa = []
    #for i in range(np.size(dens)):
    #    inte = []
    #    for j in range(i):
    #        inte.append( gdel[j] * 1.0/(np.sqrt(fpro[i]*fpro[i]-fpro[j]*fpro[j])) )        
    #    summa.append(np.trapz(inte, x=fpro[0:i]))
    #rad = konst.c/np.pi * np.array(summa)
    II = np.zeros_like(fpro)
    for j in range(1, len(gdel)):
        for i in range(1, j+1):
            II[j] = II[j] + 2.0*np.pi*gdel[i]*(np.arcsin(fpro[i]/fpro[j]) - np.arcsin(fpro[i-1]/fpro[j]))
            
    rad = k3*II
    return rad, dens, fpro, gdel
