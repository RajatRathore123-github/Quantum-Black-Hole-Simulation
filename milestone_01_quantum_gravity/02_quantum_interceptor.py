import math
import time
import sys

class QuantumInterceptorAgent:
    """
    This agent represents the rules of Loop Quantum Gravity.
    It monitors density thresholds and intercepts the physics engine 
    before an infinite singularity can form.
    """
    def __init__(self):
        # In real physics, the Planck Density is the theoretical upper limit 
        # where spacetime structure resists further compression (approx 5.1e96 kg/m³)
        self.max_allowed_density = 5.1e96 

    def analyze_telemetry(self, current_radius, current_density):
        """
        The agent evaluates data at each step of the collapse.
        Returns a command string telling the core engine what to do.
        """
        # If density hits or breaches the Planck limit, trigger an immediate override
        if current_density >= self.max_allowed_density:
            return "TRIGGER_BOUNCE"
        # If it gets dangerously close, issue a structural warning
        elif current_density > 1.0e90:
            return "ACTIVATE_TORSION_BRAKES"
        # Otherwise, the system remains within normal (though extreme) limits
        return "CONTINUE_COLLAPSE"
    
def run_simulation():
        print("=" * 65)
        print("   PHASE 2: DEPLOYING THE QUANTUM INTERCEPTOR AGENT")
        print("=" * 65)
    
        # Instantiate our intelligent monitoring agent
        agent = QuantumInterceptorAgent()
        
        # Target: Sagittarius A* physical attributes
        G = 6.6743e-11
        c = 299792458
        bh_mass_kg = 4100000 * 1.989e30
        
        # We start deep inside the event horizon at a radius of 1,000 meters
        radius = 1000.0
        step = 0
        is_bouncing = False

        print("[SYSTEM] Quantum Interceptor Agent: ONLINE and monitoring telemetry...")
        print("-" * 65)
        time.sleep(1.5)
    
        # Simulation loop
        while radius > 0:
            step += 1
            
            # Calculate current volume and density using classical mechanics
            volume = (4/3) * math.pi * (radius ** 3)
            density = bh_mass_kg / volume
            
            # Pass telemetry data to our AI Agent for a verdict
            agent_verdict = agent.analyze_telemetry(radius, density)

            # Standard display formatting
            sys.stdout.write(
                f"\rStep: {step:02d} | Radius: {radius:10.2e} m | Density: {density:10.2e} kg/m³"
            )
            sys.stdout.flush()
            time.sleep(0.3) # Slowed down so you can watch the telemetry change
    
            # Agent logic handles the engine state based on physical thresholds
            if agent_verdict == "ACTIVATE_TORSION_BRAKES":
                print(f"\n\n[AGENT ALERT] Torsion thresholds breached! Activating quantum constraints.")
                time.sleep(1.0)
                
            elif agent_verdict == "TRIGGER_BOUNCE":
                print(f"\n\n" + "#" * 65)
                print(" [CRITICAL INTERCEPTION] QUANTUM AGENT OVERRIDE")
                print("#" * 65)
                print(f" -> Gravity collapsed matter down to a safe floor of: {radius:.2e} meters.")
                print(f" -> Prevented division by zero! Max density capped at: {density:.2e} kg/m³")
                print(" -> Reversing physical vectors: Force flipped from ATTRACTIVE to REPULSIVE.")
                print(" -> Space expanding. Matter converting to primordial energy.")
                print(" [SYSTEM STATE] COSMIC BOUNCE INITIALISED. NEW UNIVERSE BORN.")
                print("#" * 65 + "\n")
                is_bouncing = True
                break
            
            # If no bounce is triggered, gravity crushes the radius tighter for the next loop
            # We shrink the radius dramatically at each step to accelerate our descent
            radius *= 0.1

        if not is_bouncing:
            print("\n[ERROR] Simulation failed. Singularity formed. System crashed.")   

if __name__ == "__main__":
    run_simulation()
    