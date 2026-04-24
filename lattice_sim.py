import numpy as np
import matplotlib.pyplot as plt

def style_plot(ax, title):
    """Applies a 'Deep Tech' R&D aesthetic to the chart."""
    ax.set_facecolor('#0b0e14')  # Industrial dark background
    # Hexagonal-style grid effect
    ax.grid(True, color='#1f2937', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_title(title, color='#e5e7eb', fontsize=14, fontweight='bold', loc='left', pad=20)
    ax.set_xlabel("SIMULATION DISTANCE (nm)", color='#9ca3af', fontsize=10)
    ax.set_ylabel("STABILITY INDEX / PRESSURE", color='#9ca3af', fontsize=10)
    ax.tick_params(colors='#6b7280', labelsize=9)
    for spine in ax.spines.values():
        spine.set_edgecolor('#374151')

def run_lattice_simulation():
    # Simulation Parameters
    x = np.linspace(5, 100, 200) # 5nm to 100nm range
    
    # Simulating Lattice Stability (The 'Engine' health)
    stability = 0.98 - (0.05 * np.exp(-0.05 * x)) + np.random.normal(0, 0.002, 200)
    
    # Simulating Energy Flux (The Fossil Fuel Replacement potential)
    energy_flux = 1 / (x**0.5) + np.random.normal(0, 0.005, 200)

    fig, ax1 = plt.subplots(figsize=(12, 7), facecolor='#0b0e14')

    # Plot 1: Lattice Stability (Electric Cyan)
    ax1.plot(x, stability, color='#22d3ee', linewidth=2.5, label='Lattice Structural Integrity', alpha=0.9)
    ax1.fill_between(x, stability - 0.015, stability + 0.015, color='#22d3ee', alpha=0.05)
    
    # Highlight the Critical Stress Zone (5nm - 50nm)
    ax1.axvspan(5, 50, color='#ef4444', alpha=0.1, label='Critical Stress Zone')
    ax1.annotate('OPTIMAL EXTRACTION RANGE', xy=(25, 0.95), xytext=(40, 0.90),
                 color='#ef4444', fontsize=9, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color='#ef4444'))

    # Plot 2: Energy Flux (Neon Amber)
    ax2 = ax1.twinx()
    ax2.plot(x, energy_flux, color='#fbbf24', linewidth=2, linestyle=':', label='Vacuum Energy Flux')
    ax2.set_ylabel("POTENTIAL ENERGY YIELD", color='#fbbf24', fontsize=10)
    ax2.tick_params(axis='y', colors='#fbbf24')

    # Final Styling
    style_plot(ax1, "GFL | QUANTUM LATTICE ANALYSIS")
    
    # Combined Legend
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc='upper right', 
               facecolor='#111827', edgecolor='#374151', labelcolor='#e5e7eb')

    # Watermark for Press Authenticity
    fig.text(0.15, 0.03, 'CONFIDENTIAL R&D: GRANDFATHER LEGACY | ZERO-HUMAN ARCHITECTURE | 2.2s KERNEL BENCHMARK', 
             fontsize=8, color='#4b5563', alpha=0.6, family='monospace')

    plt.tight_layout()
    
    # Save for Media Kit
    filename = 'lattice_analysis.png'
    plt.savefig(filename, facecolor='#0b0e14', dpi=300)
    print(f"Success: {filename} generated with R&D styling.")
    plt.show()

if __name__ == "__main__":
    run_lattice_simulation()
