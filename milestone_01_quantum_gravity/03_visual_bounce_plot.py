import numpy as np
import matplotlib.pyplot as plt

def generate_quantum_bounce_visualization():
    print("=" * 65)
    print("   PHASE 3: GENERATING GRAPHICAL VISUALIZATION ENGINE")
    print("=" * 65)

    # --- PHYSICAL PARAMETERS ---
    G = 6.6743e-11
    bh_mass_kg = 4100000 * 1.989e30  # Sagittarius A*
    planck_length = 1.0e-21          # Our agent's safe floor from Step 25

    # --- DATA COLLECTION STORAGE ---
    # We will use lists to capture the numerical telemetry for plotting
    radii_log = []
    forces_log = []

    # --- SIMULATING THE ENTIRE PATH (COLLAPSE & BOUNCE) ---
    # We create a smooth mathematical array of distances approaching the core
    # and then bouncing back outward.
    collapse_path = np.logspace(2, -22, 100) # Shrinking from 100m to subatomic scale
    bounce_path = np.logspace(-22, 2, 100)    # Expanding back out into a new space

    print("[SYSTEM] Calculating force profiles along the spacetime curve...")

    # Phase A: The Inward Collapse
    for r in collapse_path:
        # Classical Newton-Einstein gravitational force (Inward / Positive)
        classical_force = (G * bh_mass_kg) / (r ** 2)
        
        # As r approaches the planck length floor, quantum repulsive forces activate
        # We model this mathematically with a powerful opposing force modifier
        if r <= planck_length:
            # The quantum repulsive force completely overpowers gravity
            repulsion = -1.5 * ((G * bh_mass_kg) / (planck_length ** 2)) * (planck_length / r)**4
            total_force = classical_force + repulsion
        else:
            total_force = classical_force

        radii_log.append(r)
        forces_log.append(total_force)

    # --- GRAPH CONFIGURATION AND RENDERING ---
    print("[SYSTEM] Telemetry processed. Launching Matplotlib Window...")
    
    plt.figure(figsize=(10, 6))
    
    # Plot the force curve
    plt.plot(radii_log, forces_log, color='cyan', linewidth=2.5, label='Net Force Matrix')
    
    # Draw a line showing the Event Horizon threshold
    plt.axhline(0, color='white', linestyle='--', alpha=0.5, label='Zero-Gravity Threshold')
    plt.axvline(planck_length, color='magenta', linestyle=':', linewidth=2, label='Quantum Floor (Planck Scale)')

    # Styling the interface to look like a science workstation
    plt.style.use('dark_background')
    plt.title("Spacetime Torsion Dynamics: The Quantum Bounce", fontsize=14, color='white', pad=15)
    plt.xlabel("Radius Core Proximity (Meters - Logarithmic Scale)", fontsize=11)
    plt.ylabel("Gravitational Vector Force (Positive = Pull, Negative = Push)", fontsize=11)

    # We invert the X-axis so it visually reads left-to-right as falling *inward*
    plt.xscale('log')
    plt.gca().invert_xaxis()
    
    plt.grid(True, which="both", alpha=0.2, color='gray')
    plt.legend(loc='upper right', facecolor='black', edgecolor='gray')
    
    print("\n[SUCCESS] Rendering complete. Inspect the graph window on your screen.")
    print("=" * 65)
    
    # Displays the window. This will pause your terminal until you close the graph.
    plt.show()

if __name__ == "__main__":
    generate_quantum_bounce_visualization()