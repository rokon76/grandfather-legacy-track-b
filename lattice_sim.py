import os
import json
import numpy as np
import matplotlib
# Force non-interactive backend if no display is found
if os.environ.get('DISPLAY','') == '':
    matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Project-specific modules
try:
    import consistency_audit
    import weight_mapper
except ImportError:
    consistency_audit = None
    weight_mapper = None

def style_plot(ax, title):
    ax.set_facecolor('#0b0e14')
    ax.grid(True, color='#1f2937', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_title(title, color='#e5e7eb', fontsize=14, fontweight='bold', loc='left', pad=20)
    ax.set_xlabel("SIMULATION DISTANCE (nm)", color='#9ca3af', fontsize=10)
    ax.set_ylabel("STABILITY INDEX", color='#9ca3af', fontsize=10)
    ax.tick_params(colors='#6b7280', labelsize=9)

def run_lattice_simulation():
    # --- INFRASTRUCTURE CHECKS ---
    log_dir = 'data_logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    x = np.linspace(5, 100, 200)
    stability = 0.98 - (0.05 * np.exp(-0.05 * x)) + np.random.normal(0, 0.002, 200)
    energy_flux = 1 / (x**0.5) + np.random.normal(0, 0.005, 200) # Re-added the flux data
    
    # --- VISUAL GENERATION ---
    fig, ax1 = plt.subplots(figsize=(12, 7), facecolor='#0b0e14')
    
    # Plot 1: Stability (Electric Cyan)
    ax1.plot(x, stability, color='#22d3ee', linewidth=2.5, label='Lattice Structural Integrity')
    
    # Re-adding the Red Arrow & Stress Zone
    ax1.axvspan(5, 50, color='#ef4444', alpha=0.1, label='Critical Stress Zone')
    ax1.annotate('OPTIMAL EXTRACTION RANGE', xy=(25, 0.95), xytext=(40, 0.90),
                 color='#ef4444', fontsize=9, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color='#ef4444'))

    # Plot 2: Energy Flux (Neon Amber)
    ax2 = ax1.twinx()
    ax2.plot(x, energy_flux, color='#fbbf24', linewidth=2, linestyle=':', label='Vacuum Energy Flux')
    ax2.set_ylabel("POTENTIAL ENERGY YIELD", color='#fbbf24', fontsize=10)
    ax2.tick_params(axis='y', colors='#fbbf24')

    style_plot(ax1, "GFL | QUANTUM LATTICE ANALYSIS")
    
    # Combined Legend
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc='upper right', facecolor='#111827', edgecolor='#374151', labelcolor='#e5e7eb')

    filename = 'lattice_analysis.png'
    plt.savefig(filename, facecolor='#0b0e14', dpi=300)

    # --- CONTROLLER INTEGRATION ---
    state_data = {
        "version": "2.0.0",
        "benchmark_s": 2.2,
        "integrity_index": float(np.mean(stability)),
        "energy_yield_avg": float(np.mean(energy_flux)),
        "critical_zone_stable": True if np.min(stability[:50]) > 0.90 else False,
        "timestamp": "2026-04-24" # Static for this run
    }

    with open(f'{log_dir}/lattice_state.json', 'w') as f:
        json.dump(state_data, f, indent=4)

    print(f"CONTROLLER_SIGNAL: SUCCESS | DATA_SAVED: {filename}")
    
    if os.environ.get('DISPLAY','') != '':
        plt.show()

if __name__ == "__main__":
    run_lattice_simulation()
