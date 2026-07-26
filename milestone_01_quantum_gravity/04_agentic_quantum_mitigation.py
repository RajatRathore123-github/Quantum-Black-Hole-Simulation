import numpy as np
import time
import random

class MitigationAgent:
    """
    The AI Quantum Medic. Its job is to detect state decay (noise)
    caused by extreme gravity and apply correction matrices to heal the data.
    """

    def __init__(self):
        # The Pauli-X matrix acts as a Quantum NOT gate. It flips a bit back to its correct state.
        self.pauli_x = np.array([[0, 1], 
                                 [1, 0]])
        
    def inspect_and_heal(self, current_state, expected_state):
        """
        Scans the qubit vector matrix. If gravity flipped the bit,
        the agent applies the Pauli-X matrix to fix it.
        """
        # If the dot product is 1, they are perfectly identical. If 0, they are completely flipped.
        fidelity = np.dot(current_state, expected_state)

        if fidelity == 0:
            print("\n[AGENT INTERVENTION] Qubit corruption detected! State has flipped due to gravity.")
            print(" -> Status: Activating Quantum Error Mitigation...")
            time.sleep(1)
            
            # Heal the state by multiplying it by the Pauli-X correction gate
            healed_state = np.dot(self.pauli_x, current_state)
            print(" -> Status: Correction Gate applied successfully. State Matrix restored.")
            return healed_state, True
        
        return current_state, False
    
def run_mitigated_simulation():
    print("=" * 65)
    print("   PHASE 5: AGENTIC QUANTUM ERROR MITIGATION ENGINE")
    print("=" * 65)
    time.sleep(1)

    # Define our clean, ideal quantum state |0> (Stable particle before collapse)
    ideal_state = np.array([1, 0])
    current_state = ideal_state.copy()
    
    agent = MitigationAgent()

    print("[SYSTEM] Ideal Quantum State locked in: [1, 0]")
    print("[SYSTEM] AI Mitigation Agent deployed to circuit baseline.")
    print("-" * 65)
    time.sleep(1.5)

    # We simulate a 5-step descent deeper into the high-noise gravity core
    for step in range(1, 6):
        print(f"\nStep {step:02d}: Approaching Core... Gravity scale increasing.")
        time.sleep(0.5)
        
        # Determine if gravity corrupts the quantum state at this step (40% chance of noise injection)
        noise_trigger = random.random() < 0.4

        if noise_trigger:
            # Gravity injects a bit-flip error, turning [1, 0] into [0, 1]
            current_state = np.array([0, 1])
            print("[ALERT] Gravitational noise injected. Qubit state destabilised.")
        else:
            print("[INFO] Spacetime flux stable. No environmental errors detected.")
            
        # Call our AI Agent to analyze the telemetry and heal the circuit if necessary
        current_state, was_healed = agent.inspect_and_heal(current_state, ideal_state)
        
        if was_healed:
            print(f"[SYSTEM] Step {step:02d} verified: Circuit running with 100% Fidelity.")
        time.sleep(1)

    print("\n" + "=" * 65)
    print(" [SUCCESS] CORE CALCULATIONS COMPLETE WITH ZERO DATA LOSS")
    print("           Simulation safely bypassed quantum decoherence.")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    run_mitigated_simulation()