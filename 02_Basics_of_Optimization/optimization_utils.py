import numpy as np
import matplotlib.pyplot as plt

# geometric proprieties of the tube -------------------
L = 0.2            # length of the porous material (meters)
F_CUT = 1000       # the highest frequency we are interested in (Hz)

# physical proprieties of air -------------------
C0    = 343.0      # sound speed
RHO0  = 1.2043     # fluid density
MU    = 0.183e-4   # dynamic viscosity
CP    = 1004       # specific heat at constant pressure
GAMMA = 1.4        # adiabatic exponent
KAPPA = 0.259e-1   # heat conductivity  
PR    = 0.71       # prandtl number

# some constants needed for JCAL model ----------
P0 = RHO0*C0**2/GAMMA
K0 = GAMMA*P0
ETA = 1.81e-5


N_FREQS = 500 
freqs = np.linspace(1, F_CUT, N_FREQS)
omegas = 2 * np.pi * freqs


class AirMaterial:
    def __init__(self, name="Air"):
        self.name = name

    def get_JCAL_params(self, omega):
        # Effective bulk modulus and density for pure air
        K_eff = RHO0 * (C0 ** 2)
        rho_eff = RHO0
        return K_eff, rho_eff

class PorousMaterial:
    def __init__(self, name, phi, sigma, alpha, Lambda, LambdaP, k0p, k0=None):
        self.name = name
        self.phi = phi
        self.sigma = sigma
        self.alpha = alpha
        self.Lambda = Lambda
        self.LambdaP = LambdaP
        self.k0p = k0p
        self.k0 = k0 if k0 is not None else ETA / sigma

    def get_JCAL_params(self, omega):
        G1 = self.sigma * self.phi / (self.alpha * RHO0 * omega)
        G2 = 4 * self.alpha**2 * RHO0 * ETA * omega / (self.sigma**2 * self.phi**2 * self.Lambda**2)
        Gp1 = self.phi * ETA / (RHO0 * PR * self.k0p * omega)
        Gp2 = 4 * PR * RHO0 * self.k0p**2 * omega / (ETA * self.phi**2 * self.LambdaP**2)

        rho_eff = (RHO0 * self.alpha / self.phi) * (1 - 1j * G1 * np.sqrt(1 + 1j * G2))
        K_eff = (K0 / self.phi) * (1 / (GAMMA - (GAMMA - 1) / (1 - 1j * Gp1 * np.sqrt(1 + 1j * Gp2))))

        return K_eff, rho_eff


# Preset materials
MATERIALS = {
    "spf": PorousMaterial("SPF", phi=0.999, sigma=5678, alpha=1.00, Lambda=1.472e-4, LambdaP=2.443e-4, k0p=4.5866e-9, k0=3.1877e-9),
    "acoustic_foam": PorousMaterial("Acoustic Foam", phi=0.98, sigma=8700, alpha=1.42, Lambda=7.5e-5, LambdaP=2.1e-4, k0p=3.5e-9),
    "melamine_foam": PorousMaterial("Melamine Foam", phi=0.99, sigma=10900, alpha=1.02, Lambda=1.0e-4, LambdaP=2.0e-4, k0p=1.8e-9),
    "felt": PorousMaterial("Felt", phi=0.88, sigma=120000, alpha=1.20, Lambda=1.8e-5, LambdaP=5.5e-5, k0p=2.0e-10),
    "glass_wool": PorousMaterial("Glass Wool", phi=0.95, sigma=40000, alpha=1.05, Lambda=5.0e-5, LambdaP=1.0e-4, k0p=8.0e-10),
    "air": AirMaterial(name="Air")
}     

# Transfer matrix function for a single layer
def get_T_layer(omega, l_por, mat):
    K_eff, rho_eff = mat.get_JCAL_params(omega)
    Zf = np.sqrt(K_eff * rho_eff)
    kf = omega / np.sqrt(K_eff / rho_eff)

    t = np.zeros((2, 2), dtype=complex)
    t[0, 0] = np.cos(kf * l_por)
    t[1, 1] = np.cos(kf * l_por)
    t[0, 1] = 1j * Zf * np.sin(kf * l_por)
    t[1, 0] = 1j / Zf * np.sin(kf * l_por)
    return t


def R_from_T(T):
    Z0 = (RHO0 * C0)
    return (T[0, 0] - T[1, 0] * Z0) / (T[0, 0] + T[1, 0] * Z0)

def compute_spectrum(lengths, materials):
    """Computes R and absorption across all frequencies for an arbitrary N-layer sandwich structure.
    
    Parameters:
    -----------
    lengths : list or array of layer thicknesses [l_1, l_2, ..., l_N] (meters)
    materials : list of PorousMaterial instances [mat_1, mat_2, ..., mat_N]
    """
    R = np.zeros(N_FREQS, dtype=complex)
    
    for i in range(N_FREQS):
        omega = omegas[i]
        
        # Start with 2x2 Identity Matrix: I = [[1, 0], [0, 1]]
        T_total = np.eye(2, dtype=complex)
        
        # Multiply T = T_1 @ T_2 @ ... @ T_N
        for l_layer, mat in zip(lengths, materials):
            if l_layer > 0:  # Skip zero-thickness layers
                T_layer = get_T_layer(omega, l_layer, mat)
                T_total = T_total @ T_layer
                
        R[i] = R_from_T(T_total)
        
    absorption = 1.0 - np.abs(R)**2
    return R, absorption


def setup_abs_axis():
    """Formats absorption coefficient axis (limits, labels, grid, legend)."""
    plt.xlabel('Frequency / Hz')
    plt.ylabel('Absorption Coefficient')
    plt.xlim(0, F_CUT)
    plt.ylim(0, 1)
    plt.grid(True)
    plt.legend()

def setup_r_axis():
    """Formats reflection coefficient axis (limits, labels, grid, legend)."""
    plt.xlabel('Frequency / Hz')
    plt.ylabel('Magnitude of Reflection Coefficient')
    plt.xlim(0, F_CUT)
    plt.ylim(0, 1)
    plt.grid(True)
    plt.legend()