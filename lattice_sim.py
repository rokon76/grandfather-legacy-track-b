import numpy as np
import matplotlib.pyplot as plt

def simulate_loading(substrate, time_steps=100):
    """Simulates H-loading saturation based on substrate stability."""
    # Stability coefficients derived from Track A
    stability = {
        'Gold': 0.5,      # High stress, slower loading
        'Germanium': 0.8, # Improved stability
        'Graphite': 0.95  # Maximum lattice integrity
    }
    
    coeff = stability.get(substrate, 0.5)
    time = np.linspace(0, 10, time_steps)
    # Saturation curve: 1 - exp(-kt)
    saturation = 1 - np.exp(-coeff * time)
    return time, saturation

def main():
    print("--- Track B: Pd-H Lattice Kinetics ---")
    
    test_materials = ['Gold', 'Germanium', 'Graphite']
    plt.figure(figsize=(10, 6))
    
    for mat in test_materials:
        t, s = simulate_loading(mat)
        plt.plot(t, s, label=f"Pd on {mat}")
        final_sat = s[-1] * 100
        print(f"✅ {mat} Substrate: {final_sat:.1f}% Saturation achieved.")

    plt.axhline(y=0.9, color='r', linestyle='--', label='Target Saturation (90%)')
    plt.xlabel('Time (Arbitrary Units)')
    plt.ylabel('Hydrogen Saturation (H/Pd Ratio)')
    plt.title('Hydrogen Loading Kinetics vs. Substrate Stability')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig('loading_kinetics.png')
    print("\n[SUCCESS] Kinetic profile saved as loading_kinetics.png")

if __name__ == "__main__":
    main()
