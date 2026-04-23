import numpy as np
import matplotlib.pyplot as plt

def calculate_lattice_expansion(loading_ratio):
    """
    Calculates the lattice constant (a) for a Palladium-Hydrogen system.
    Pd starts as an FCC lattice with a_0 ≈ 3.89 Å.
    """
    a_0 = 3.890 
    expansion_coeff = 0.063
    return a_0 * (1 + expansion_coeff * loading_ratio)

def calculate_kinetics(temp_celsius, thickness_mm):
    """
    Calculates the diffusion coefficient (D) and estimated saturation time.
    Formula: D = D0 * exp(-Ea / (R * T))
    """
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
    # --- CONFIGURATION ---
    thickness = 0.5  # Sample thickness in mm
    test_temps = [25, 100, 300]  # Temperatures to compare
    
    print(f"--- Pd-H Loading Analysis (Sample: {thickness}mm) ---")
    print(f"{'Temp (°C)':<10} | {'Diffusion (m^2/s)':<20} | {'Est. Time'}")
    print("-" * 55)
    
    results_time = []
    
    for temp in test_temps:
        D, time_hours = calculate_kinetics(temp, thickness)
        results_time.append(time_hours)
        
        if time_hours < 1:
            time_str = f"{time_hours*60:.2f} mins"
        else:
            time_str = f"{time_hours:.2f} hours"
            
        print(f"{temp:<10} | {D:<20.2e} | {time_str}")

    # --- VISUALIZATION ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Plot 1: Lattice Expansion
    ratios = np.linspace(0.0, 1.0, 100)
    a_vals = [calculate_lattice_expansion(r) for r in ratios]
    ax1.plot(ratios, a_vals, color='#2c3e50', linewidth=2)
    ax1.axvspan(0.6, 1.0, color='red', alpha=0.1, label='Critical Beta-Phase')
    ax1.set_title('Physical Expansion vs. Loading')
    ax1.set_xlabel('Loading Ratio (H/Pd)')
    ax1.set_ylabel('Lattice Constant (Å)')
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # Plot 2: Temperature Sensitivity (Log Scale)
    ax2.bar([f"{t}°C" for t in test_temps], results_time, color=['#34495e', '#e67e22', '#c0392b'])
    ax2.set_yscale('log')
    ax2.set_title('Time to Saturation (Log Scale)')
    ax2.set_ylabel('Hours')
    ax2.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    print("\nSimulation complete. Displaying analysis charts...")
    plt.show()

if __name__ == "__main__":
    main()
