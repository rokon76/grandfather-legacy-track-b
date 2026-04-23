import numpy as np

def calculate_lattice_expansion(loading_ratio):
    """
    Calculates the lattice constant (a) for a Palladium-Hydrogen system.
    Pd starts as an FCC lattice with a_0 ≈ 3.89 Å.
    As H is loaded, the lattice expands.
    """
    # Initial lattice constant for pure Palladium in Angstroms
    a_0 = 3.890 
    
    # Empirical expansion coefficient for Pd-H systems
    # Roughly: a = a_0 * (1 + 0.063 * loading_ratio)
    expansion_coeff = 0.063
    
    current_a = a_0 * (1 + expansion_coeff * loading_ratio)
    return current_a

def main():
    # Define loading ratios (H/Pd) from 0.0 to 1.0
    ratios = np.linspace(0.0, 1.0, 11)
    
    print(f"{'Loading Ratio (H/Pd)':<20} | {'Lattice Constant (Å)':<20}")
    print("-" * 45)
    
    for r in ratios:
        a_n = calculate_lattice_expansion(r)
        print(f"{r:<20.1f} | {a_n:<20.4f}")

if __name__ == "__main__":
    main()
