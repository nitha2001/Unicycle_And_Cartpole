# Unicycle_And_Cartpole
Trajectory planning and control for a unicycle system, involving obstacle avoidance and spline-based trajectory generation and an  Implementation of partial feedback linearization and energy shaping control for a cart-pole system, including simulation of upright stabilization.

## Key Components
**Unicycle System Trajectory Planning**: Developed a trajectory planning algorithm using cubic splines to navigate a unicycle from an initial to a final position while avoiding obstacles. The code computes smooth paths in flat output space, ensuring continuity and obstacle avoidance.

**Unicycle Controller Implementation**: Built a controller based on derived input formulas to ensure the unicycle follows the planned trajectory. This controller was tested and validated through simulations.

**Cart-Pole System Energy Shaping**: Implemented an energy shaping controller to stabilize an underactuated cart-pole system. The controller was designed to control the cart's position and the pendulum's swing using partial feedback linearization. Stability was tested with various initial conditions through simulation.

**Simulation and Visual Output**: Simulated all control systems, displaying both planned and actual trajectories. The cart-pole simulation demonstrates successful stabilization through energy shaping and damping, while the unicycle simulation validates the obstacle avoidance path.

## Key Files:

- `unicycle_spline.py`: Implements trajectory planning for the unicycle system.
- `unicycle_input.py`: Implements the control strategy for the unicycle based on differential flatness.
- `cartpole.py`: Controller implementation for energy shaping in the cart-pole system.
- `simulate_unicycle.py and cartpole_sim.py`: Scripts to simulate and visualize the system dynamics.
