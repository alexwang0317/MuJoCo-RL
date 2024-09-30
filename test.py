import mujoco_py
import os
import numpy as np

# Load a simple MuJoCo environment (e.g., a humanoid or cartpole)
xml_path = mujoco_py.utils.discover_mujoco() + "/model/humanoid.xml"
model = mujoco_py.load_model_from_path(xml_path)
sim = mujoco_py.MjSim(model)

# Create a viewer to visualize the simulation
viewer = mujoco_py.MjViewer(sim)

# Run a basic simulation loop
for step in range(1000):  # Run the simulation for 1000 steps
    # Set random control values as an example
    control_values = np.random.uniform(-1, 1, model.nu)
    sim.data.ctrl[:] = control_values
    
    # Step the simulation forward
    sim.step()
    
    # Render the scene in the viewer
    viewer.render()

    # Check for NaN or unusual values (simple test)
    if np.isnan(sim.data.qpos).any():
        print(f"Step {step}: NaN detected in position values!")
        break

print("Simulation completed.")
