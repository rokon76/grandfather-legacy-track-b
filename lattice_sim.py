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

def main():
    # Define a smoother range for a clean curve
    ratios = np.linspace(0.0, 1.0, 100)
    lattice_constants = [calculate_lattice_expansion(r) for r in ratios]
    
    # Create the visualization
    plt.figure(figsize=(10, 6))
    plt.plot(ratios, lattice_constants, color='#2c3e50', linewidth=2, label='FCC Expansion')
    
    # Highlight the critical loading zone (Beta-phase)
    plt.axvspan(0.6, 1.0, color='red', alpha=0.1, label='Critical Loading Zone (Beta)')
    
    plt.title('Pd-H Lattice Expansion vs. Loading Ratio', fontsize=14)
    plt.xlabel('Loading Ratio (H/Pd)', fontsize=12)
    plt.ylabel('Lattice Constant (Å)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    print("Simulation complete. Displaying expansion curve...")
    plt.show()

if __name__ == "__main__":
    main()
