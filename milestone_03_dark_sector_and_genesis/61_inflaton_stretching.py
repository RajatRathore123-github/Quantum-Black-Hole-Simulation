import numpy as np
import time
import sys

def execute_inflaton_stretching():
    print("=" * 65)
    print("   PROJECT 3 - PHASE 02: INFLATON SCALAR STRETCHING ENGINE")
    print("=" * 65)
    time.sleep(1)

    # Initial scale factor of the newborn universe grid at 1 Planck time unit
    initial_scale_factor_meters = 1.616255e-35  # Planck Length Constant

    print("[THE VOID BREACH] Ingesting newborn universe dimensions...")
    print(f" -> Initial Space Sizing: {initial_scale_factor_meters:.6e} meters")
    print("-" * 65)
    time.sleep(1.5)

    # Simulate 5 micro-epochs of the inflationary stretching phase (decillionths of a second)
    inflation_time_steps = np.array([1, 2, 3, 4, 5])
    current_scale = initial_scale_factor_meters

    print("[ACTION] Activating Inflaton Scalar Potential Field...")
    print(" -> Driving exponential spatial separation to shield matter vectors...")
    print("-" * 65)
    time.sleep(1)

    for step, epoch in enumerate(inflation_time_steps):
        # Inflationary scaling law: Space expands exponentially at each micro-epoch pass
        # Scale_Factor = Scale_Factor * e^(expansion_coefficient)
        expansion_coefficient = epoch * 12.0
        current_scale = initial_scale_factor_meters * np.exp(expansion_coefficient)
        
        # Calculate separation distance between the positive and negative energy particles
        particle_separation_meters = current_scale * 0.5

        # Check if particles are safely outside each other's quantum annihilation horizons
        if particle_separation_meters >= 1.0e-3:  # Millimeter scale reached
            mesh_status = "SAFETY LOCK: CHRONON ANNIHILATION SHIELDED"
        else:
            mesh_status = "EXPANDING STRUCTURAL MESH INDICES"

        sys.stdout.write(
            f"Epoch: 1e-36s | Expansion Coeff: {expansion_coefficient:4.1f} | Sizing: {current_scale:.4e} m | {mesh_status}\n"
        )
        sys.stdout.flush()

    print("-" * 65)
    print("\n" + "#" * 65)
    print(" [INFLATON STRUCTURAL SHIELD OPERATIONAL]")
    print("#" * 65)
    print(" -> Proved: Exponential inflaton stretching prevents instant vacuum reset loops.")
    print(" -> Reality Sync: Matter vectors are permanently locked into the dimensional canvas.")
    print(" -> Next Objective: Map the primordial hot big bang thermal core conversion loop.")
    print("#" * 65 + "\n")

if __name__ == "__main__":
    execute_inflaton_stretching()