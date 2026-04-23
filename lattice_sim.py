import numpy as np
import matplotlib.pyplot as plt

def calculate_kinetics(temp_celsius, thickness_mm):
    """
    Calculates the diffusion coefficient (D) and estimated saturation time.
    D = D0 * exp(-Ea / (R * T))
    """
    # Constants for H in Pd
    D0 = 2.9e-7  # Pre-exponential factor (m^2/s)
    Ea = 22200   # Activation energy (J/mol)
    R = 8.314    # Gas constant (J/mol*K)
    
    T_kelvin = temp_celsius + 273.15
    D = D0 * np.exp(-Ea / (R * T_kelvin))
    
    # Time to reach ~90% saturation (Approximation: t = L^2 / D)
    # L is half-thickness for double-sided loading
    L = (thickness_mm / 1000) / 2
    time_seconds = (L**2) / D
    return D, time_seconds / 3600  # Returns D and Time in Hours

def main():
    temp = 25  # Room Temperature in Celsius
    thickness = 1.0  # 1mm Pd sample
    
    D, time_hours = calculate_kinetics(temp, thickness)
    
    print(f"--- Kinetic Analysis ---")
    print(f"Temperature: {temp}°C")
    print(f"Sample Thickness: {thickness}mm")
    print(f"Diffusion Coefficient: {D:.2e} m^2/s")
    print(f"Est. Time to Saturation: {time_hours:.2f} hours")
    
    # Generate visualization for expansion as before
    ratios = np.linspace(0.0, 1.0, 100)
    a_0 = 3.890
    lattice_constants = [a_0 * (1 + 0.063 * r) for r in ratios]
    
    plt.figure(figsize=(10, 6))
    plt.plot(ratios, lattice_constants, color='#2c3e50', label='Lattice Expansion')
    plt.axvspan(0.6, 1.0, color='red', alpha=0.1, label='Beta-Phase Target')
    plt.title(f'Pd-H System: {time_hours:.1f}hr Loading Estimate at {temp}°C')
    plt.xlabel('Loading Ratio (H/Pd)')
    plt.ylabel('Lattice Constant (Å)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    main()
