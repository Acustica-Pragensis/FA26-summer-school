import numpy as np
import matplotlib.pyplot as plt

E = 170e+9      # (Pa) young modulus
nu = 0.28       # (-) poisson ratio
rho_p = 2329    # kg/m^3 plate density

def get_freq(a,h,p,d, m, n):
    
    r = d**2/p**2

    c1 = 2.39 * ( (h**2)/(p**2) - (0.1311 * h)/p + 0.475 + (p / a))
    c2 = 1.48 * ((h / p) + 0.165 + (p / a))**2 + 1.81

    freq = 0.201*np.sqrt(E*h**2/(12*(1-nu**2) * rho_p))*(1/ (a**2)) * np.sqrt((m + n)**5.6 / (m*n)**1.16)
    freq *= (r + c1) / (c2* r + c1)
    return freq