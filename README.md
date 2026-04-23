Grandfather Legacy: Track B Mining Guide
Welcome to the simulation layer of the Grandfather Legacy subnet. Your goal is to utilize computational physics to optimize hydrogen loading kinetics within metal lattices.

🎯 The Mission
To earn rewards, you must find a material configuration that achieves a loading time of less than 2.2 seconds.

Current World Record: 2.13s

Target Benchmark: 109.09 (9% improvement over baseline)

🚀 Quick Start: How to Mine
1. Environment Setup
Ensure you have Python 3.x installed. Clone this repository and navigate to your working directory:

Bash
git clone https://github.com/rokon76/grandfather-legacy-track-b.git
cd grandfather-legacy-track-b
2. Run the Miner Template
We provide a miner_template.py to get you started. This script simulates the physics engine and packages your results.

Bash
python miner_template.py
This will generate a submission.json file in your local directory.

3. Optimize Your Model
The template uses a placeholder for the physics logic. To beat the record, you must modify the run_physics_model() function in miner_template.py with your own proprietary AI or simulation algorithms.

4. Submit for Audit
Once you have a competitive submission.json, it must be verified by the Track A Validator.

Validation: Your submission is checked for physical consistency and compared against the global leaderboard.

Rewards: Successful breakthroughs trigger a weight boost in the incentive mechanism.

📊 Technical Specifications
Primary Material Focus: Pd-H (Palladium-Hydrogen) and Ni-H (Nickel-Hydrogen).

Key Metric: Loading time (seconds) to reach saturation.

Incentive Structure: Linear weight scaling for every 1% improvement over the 2.2s benchmark.

💡 Pro-Tip for Miners
Focus on lattice geometry and phonon coupling. The most efficient simulations often involve non-standard crystalline structures that reduce the activation energy for hydrogen migration.
