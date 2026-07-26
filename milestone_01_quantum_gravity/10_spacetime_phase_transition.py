import numpy as np
import time
import sys

class SpacetimePhaseEngine:
    """
    Models our new hypothesis: Spacetime is a dynamic phase-changing medium.
    It transitions from 'Fluid' to 'Solid' under extreme Planck-scale pressure.
    """
    def __init__(self):
        # Critical density where spacetime shifts phases (Planck Scale threshold)
        self.critical_density = 5.1e96  # kg/m³

    def calculate_spacetime_state(self, density):
        """
        Calculates the state of the spacetime medium.
        Returns the phase state and the Viscosity/Resistance factor.
        """
        if density >= self.critical_density:
            # Spacetime has frozen solid. Resistance becomes infinite!
            phase = "CRYSTALLIZED_SUPERFLUID"
            resistance = float('inf')
        elif density > 1.0e90:
            # Spacetime is thickening rapidly like a dense gel
            phase = "HIGH_VISCOSITY_GEL"
            # Exponential resistance scaling
            resistance = np.exp((density / 1.0e90))
        else:
            # Normal smooth spacetime behavior
            phase = "CONTINUOUS_FLUID"
            resistance = 1.0

        return phase, resistance

def execute_brainstorm_simulation():
    print("=" * 65)
    print("   THEORETICAL MODEL: SPACETIME PHASE TRANSITION ENGINE")
    print("=" * 65)
    time.sleep(1)

    engine = SpacetimePhaseEngine()
    
    # Target: Sagittarius A* mass scaling
    G = 6.6743e-11
    bh_mass_kg = 4100000 * 1.989e30
    
    radius = 50.0  # Closing in on the core (meters)
    step = 0
    
    print("[HYPOTHESIS] Monitoring 'Chronon' medium state during collapse...")
    print("-" * 65)
    time.sleep(1.5)

    while radius > 0:
        step += 1
        radius *= 0.5  # Inward gravitational crush
        
        # Calculate standard volume and density
        volume = (4/3) * np.pi * (radius ** 3)
        density = bh_mass_kg / volume
        
        # Query our new phase engine
        phase, resistance = engine.calculate_spacetime_state(density)
        
        # Format printing
        sys.stdout.write(
            f"\rStep: {step:02d} | Radius: {radius:8.2e} m | Phase: {phase:22s}"
        )
        sys.stdout.flush()
        time.sleep(0.5)

        if phase == "HIGH_VISCOSITY_GEL":
            print(f"\n -> [GEOMETRY DISTORTION] Spacetime is thickening. Resistance factor: {resistance:.2e}")
            time.sleep(1)
            
        elif phase == "CRYSTALLIZED_SUPERFLUID":
            print(f"\n\n" + "#" * 65)
            print(" [HYPOTHESIS CONFIRMED: THE SINGULARITY SHATTERED]")
            print("#" * 65)
            print(f" -> Matter struck the crystallized spacetime floor at {radius:.2e} meters.")
            print(" -> Result: The background fabric can no longer be compressed.")
            print(" -> Kinetic vector terminated. Inward gravity overbalanced.")
            print(" -> ACTION: Energy must deflect. Initiating cosmic rebound bounce.")
            print("#" * 65 + "\n")
            break

if __name__ == "__main__":
    execute_brainstorm_simulation()