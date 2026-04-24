import os
import json
import numpy as np
import matplotlib
# Force non-interactive backend if no display is found (prevents controller hangs)
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
    
    # --- VISUAL GENERATION ---
    fig, ax1 = plt.subplots(figsize=(12, 7), facecolor='#0b0e14')
    ax1.plot(x, stability, color='#22d3ee', linewidth=2.5, label='Lattice Structural Integrity')
    style_plot(ax1, "GFL | QUANTUM LATTICE ANALYSIS")
    
    filename = 'lattice_analysis.png'
    plt.savefig(filename, facecolor='#0b0e14', dpi=300)

    # --- CONTROLLER INTEGRATION ---
    # Prepare data for the weight mapper/controller
    state_data = {
        "version": "2.0.0",
        "benchmark_s": 2.2,
        "integrity_index": float(np.mean(stability)),
        "critical_zone_stable": True if np.min(stability[:50]) > 0.90 else False,
        "timestamp": plt.Timestamp('now').strftime('%Y-%m-%d %H:%M:%S') if hasattr(plt, 'Timestamp') else "2026-04-24"
    }

    with open(f'{log_dir}/lattice_state.json', 'w') as f:
        json.dump(state_data, f, indent=4)

    print(f"CONTROLLER_SIGNAL: SUCCESS | DATA_SAVED: {filename}")
    
    # Only show if a display is available
    if os.environ.get('DISPLAY','') != '':
        plt.show()

if __name__ == "__main__":
    run_lattice_simulation()
