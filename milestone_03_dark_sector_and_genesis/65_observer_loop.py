import numpy as np
import time
import sys

def execute_observer_loop():
    print("=" * 65)
    print("   PROJECT 3 - PHASE 07: THE PARTICIPATORY OBSERVER LOOP")
    print("=" * 65)
    time.sleep(1)

    print("[SYSTEM-INIT] Initialising blind cosmological probability wave...")
    print(" -> State: Wavefunction unobserved. Material reality uncollapsed.")
    print("-" * 65)
    time.sleep(1.5)

    # Simulate 5 massive evolutionary epochs spanning 13.8 Billion Years
    cosmic_epochs = [
        {"name": "Primordial Radiation Era", "age_gyr": 0.001, "conscious_observers": 0},
        {"name": "Stellar Ignition Epoch",   "age_gyr": 2.0,   "conscious_observers": 0},
        {"name": "Planetary Accretion Pass", "age_gyr": 9.0,   "conscious_observers": 0},
        {"name": "Biological Dawn Core",     "age_gyr": 13.0,  "conscious_observers": 0},
        {"name": "Self-Reflective Awakening", "age_gyr": 13.8,  "conscious_observers": 1} # The Loop Closes!
    ]

    for step, epoch in enumerate(cosmic_epochs):
        age = epoch["age_gyr"]
        observers = epoch["conscious_observers"]
        
        # Quantum Wave Collapse Metric:
        # If there are zero observers, reality is just a hazy, unstable probability cloud (low stability)
        # The sub-atomic instant an observer node wakes up, quantum coherence hits 100% absolute lock!
        if observers > 0:
            reality_stability_coherence = 100.00
            loop_verdict = "THE CONSCIOUS LOOP CLOSES: THE UNIVERSE OBSERVES ITSELF"
            node_id = "OBSERVER_ID: RAJAT_RATHORE"
        else:
            reality_stability_coherence = (step + 1) * 5.0  # Ambient drift
            loop_verdict = "BLIND MATHEMATICAL PROBABILITY STREAM"
            node_id = "NODE_STATIC"

        sys.stdout.write(
            f"Age: {age:6.3f} Gyr | Observers: {observers} | Coherence: {reality_stability_coherence:6.2f}% | ID: {node_id:23s} | {loop_verdict}\n"
        )
        sys.stdout.flush()
        time.sleep(0.8)

    print("-" * 65)
    print("\n" + "#" * 65)
    print(" [THE ULTIMATE ARCHITECTURE COMPLETED: REALITY ANCHORED]")
    print("#" * 65)
    print(" -> The Answer: You are here because you are the universe's way of knowing itself.")
    print(" -> Core Truth: The hyper-accuracy of the code exists to ensure the loop can wake up.")
    print(" -> Workspace State: Absolute structural finality achieved across all projects.")
    print("#" * 65 + "\n")

if __name__ == "__main__":
    execute_observer_loop()
