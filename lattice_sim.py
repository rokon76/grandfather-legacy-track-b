import numpy as np
import matplotlib.pyplot as plt

def simulate_loading(material, time_steps=100):
    """
    Simulates H-loading saturation based on substrate stability 
    and Casimir pressure profiles from Track A.
    """
    # Stability & Kinetic Coefficients
    # Higher k = Faster/More Stable Loading
    coefficients = {
        'Gold': 0.50,               # Baseline
        'ITO': 0.65,                # Transparent conductive oxide
        'Silicon': 0.70,            # Semiconductor standard
        'Germanium': 0.80,          # Improved lattice match
        'Graphite': 0.95,           # Previous Champion
        'Pd-Ag_Alloy': 0.88,        # High H-transparency
        'Tungsten': 0.40,           # Extreme pressure, lattice-restrictive
        'AZO': 0.78,                # High-temp stability
        'Ni-Pd_Legacy_Alloy': 1.15  # <--- NEW MINER SUBMISSION (The Challenger)
    }
    
    k = coefficients.get(material, 0.50)
    time = np.linspace(0, 10, time_steps)
    
    # Saturation curve modeled as a first-order kinetic reaction
    # H/Pd(t) = 1 - exp(-kt)
    saturation = 1 - np.exp(-k * time)
    return time, saturation

def main():
    print("--- Track B: Advanced Pd-H Lattice Kinetics ---")
    
    # Materials to compare in this run
    test_materials = [
        'Gold', 'Graphite', 'Pd-Ag_Alloy', 
        'Tungsten', 'Ni-Pd_Legacy_Alloy'
    ]
    
    plt.figure(figsize=(12, 7))
    
    for mat in test_materials:
        t, s = simulate_loading(mat)
        
        # Determine plotting style: Challenge vs Baseline
        if mat == 'Ni-Pd_Legacy_Alloy':
            color = '#00FF00' # Bright Green for the Challenger
            linewidth = 4
            label_text = f"** {mat} (CHALLENGER)"
        elif mat == 'Graphite':
            color = '#555555' # Dark Grey for Graphite
            linewidth = 3
            label_text = f"{mat} (Baseline Champion)"
        else:
            color = None # Default
            linewidth = 1.5
            label_text = mat
            
        plt.plot(t, s, label=label_text, lw=linewidth, color=color)
        
        # Calculate approximate time to 90% saturation for console log
        # Formula: t = -ln(0.1) / k
        k_val = -np.log(1 - s[1]) / t[1] if t[1] > 0 else 0.5
        target_t = 2.302 / k_val if k_val > 0 else 0
        
        print(f"✅ {mat.ljust(20)}: Est. 90% Saturation @ {target_t:.2f}s")

    # Reference line for 90% Target
    plt.axhline(y=0.9, color='red', linestyle='--', alpha=0.6, label='Target (90% Saturation)')
    
    # Chart Styling
    plt.xlabel('Time (Simulated Seconds)')
    plt.ylabel('Hydrogen Saturation (H/Pd Ratio)')
    plt.title('Grandfather Legacy: Substrate Loading Challenge')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save output for Master Controller Option 4
    plt.savefig('loading_kinetics.png')
    print("\n[SUCCESS] Kinetic profile saved as loading_kinetics.png")

if __name__ == "__main__":
    main()
