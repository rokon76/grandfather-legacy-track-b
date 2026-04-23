import numpy as np
import matplotlib
# Forces the script to generate an image file even if no window can open
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import os

def calculate_lattice_expansion(loading_ratio):
    a_0 = 3.890 
    expansion_coeff = 0.063
    return a_0 * (1 + expansion_coeff * loading_ratio)

def calculate_kinetics(temp_celsius, thickness_mm):
    D0 = 2.9e-7 
    Ea = 22200   
    R = 8.314    
    T_kelvin = temp_celsius + 273.15
    D = D0 * np.exp(-Ea / (R * T_kelvin))
    L = (thickness_mm / 1000) / 2
    time_seconds = (L**2) / D
    return D, time_seconds / 3600

def main():
    thickness = 0.5 
    test_temps = [25, 100, 300] 
    
    print(f"--- Pd-H Loading Analysis (Sample: {thickness}mm) ---")
    results_time = []
    for temp in test_temps:
        D, time_hours = calculate_kinetics(temp, thickness)
        results_time.append(time_hours)
        time_str = f"{time_hours*60:.2f} mins" if time_hours < 1 else f"{time_hours:.2f} hours"
        print(f"{temp}°C | {time_str}")

    # --- GENERATING IMAGE ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    ratios = np.linspace(0.0, 1.0, 100)
    a_vals = [calculate_lattice_expansion(r) for r in ratios]
    ax1.plot(ratios, a_vals, color='#2c3e50', linewidth=2)
    ax1.axvspan(0.6, 1.0, color='red', alpha=0.1, label='Beta-Phase')
    ax1.set_title('Lattice Expansion')
    ax1.set_xlabel('H/Pd Ratio')
    ax1.set_ylabel('Angstroms (Å)')

    ax2.bar([f"{t}°C" for t in test_temps], results_time, color=['#34495e', '#e67e22', '#c0392b'])
    ax2.set_yscale('log')
    ax2.set_title('Time to Saturation (Log Scale)')
    ax2.set_ylabel('Hours')

    plt.tight_layout()
    
    # This creates the file in your folder
    output_file = "lattice_analysis.png"
    plt.savefig(output_file)
    print(f"\n✅ SUCCESS: Image saved to: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()
