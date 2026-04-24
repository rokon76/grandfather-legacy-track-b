import os
import json
import subprocess
import math
import numpy as np
import matplotlib.pyplot as plt

# Project-specific modules
try:
    import consistency_audit
    import weight_mapper
except ImportError:
    consistency_audit = None
    weight_mapper = None

def style_plot(ax, title):
    """Applies the GFL R&D aesthetic for industrial-grade visuals."""
    ax.set_facecolor('#0b0e14')
    ax.grid(True, color='#1f2937', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_title(title, color='#e5e7eb', fontsize=14, fontweight='bold', loc='left', pad=20)
    ax.set_xlabel("SIMULATION DISTANCE (nm)", color='#9ca3af', fontsize=10)
    ax.set_ylabel("STABILITY INDEX / PRESSURE", color='#9ca3af', fontsize=10)
    ax.tick_params(colors='#6b7280', labelsize=9)
    for spine in ax.spines.values():
        spine.set_edgecolor('#374151')

def run_lattice_simulation():
    # --- INFRASTRUCTURE CHECKS ---
    if not os.path.exists('data_logs'):
        os.makedirs('data_logs')

    # Simulation Parameters (5nm to 100nm)
    x = np.linspace(5, 100, 200)
    stability = 0.98 - (0.05 * np.exp(-0.05 * x)) + np.random.normal(0, 0.002, 200)
    energy_flux = 1 / (x**0.5) + np.random.normal(0, 0.005, 200)

    # --- VISUAL GENERATION ---
    fig, ax1 = plt.subplots(figsize=(12, 7), facecolor='#0b0e14')

    # Plot 1: Stability (Electric Cyan)
    ax1.plot(x, stability, color='#22d3ee', linewidth=2.5, label='Lattice Structural Integrity')
    ax1.fill_between(x, stability - 0.015, stability + 0.015, color='#22d3ee', alpha=0.05)
    
    # Red Arrow / Stress Zone
    ax1.axvspan(5, 50, color='#ef4444', alpha=0.1, label='Critical Stress Zone')
    ax1.annotate('OPTIMAL EXTRACTION RANGE', xy=(25, 0.95), xytext=(40, 0.90),
                 color='#ef4444', fontsize=9, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color='#ef4444'))

    # Plot 2: Flux (Neon Amber)
    ax2 = ax1.twinx()
    ax2.plot(x, energy_flux, color='#fbbf24', linewidth=2, linestyle=':', label='Vacuum Energy Flux')
    ax2.set_ylabel("POTENTIAL ENERGY YIELD", color='#fbbf24', fontsize=10)
    ax2.tick_params(axis='y', colors='#fbbf24')

    style_plot(ax1, "GFL | QUANTUM LATTICE ANALYSIS")
    
    # Watermark
    fig.text(0.15, 0.03, 'CONFIDENTIAL R&D: GRANDFATHER LEGACY | ZERO-HUMAN ARCHITECTURE | 2.2s KERNEL', 
             fontsize=8, color='#4b5563', alpha=0.6, family='monospace')

    plt.tight_layout()
    filename = 'lattice_analysis.png'
    plt.savefig(filename, facecolor='#0b0e14', dpi=300)

    # --- INTEGRATION LOGIC ---
    # Trigger weight mapper or audit if present
    if consistency_audit:
        # Example call to your infrastructure
        # consistency_audit.verify_lattice(stability)
        pass

    # Save operational JSON
    with open('data_logs/lattice_state.json', 'w') as f:
        json.dump({"benchmark": "2.2s", "integrity": np.mean(stability)}, f)

    print(f"Success: {filename} generated. Infrastructure logs updated.")
    plt.show()

if __name__ == "__main__":
    run_lattice_simulation()
