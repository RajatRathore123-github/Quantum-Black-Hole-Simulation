import numpy as np
import time
import random

class AdvancedQuantumAgent:
    """
    An advanced AI agent capable of executing a 3-Qubit Syndrome Measurement.
    It identifies which specific qubit in an entangled chain has been corrupted
    by gravity without measuring the actual data payload.
    """
    def __init__(self):
        # Pauli-X matrix (Quantum NOT Gate) used to flip a corrupted qubit back
        self.pauli_x = np.array([[0, 1], [1, 0]])

    
    def measure_syndrome(self, current_chain):
        """
        Calculates parity checks between adjacent qubits.
        Syndrome Vector: [Comparison_1_2, Comparison_2_3]
        1 means they match (healthy), 0 means they do not match (error).
        """
        syn_1_2 = 1 if current_chain[0] == current_chain[1] else 0
        syn_2_3 = 1 if current_chain[1] == current_chain[2] else 0
        return [syn_1_2, syn_2_3]
    
    def execute_error_correction(self, current_chain, syndrome):
        """
        Decodes the syndrome vector to apply the precise quantum correction gate.
        """
        # Case 1: [1, 1] -> Both pairs match. The chain is completely healthy.
        if syndrome == [1, 1]:
            return current_chain, "NO_ERROR"

        # Case 2: [0, 1] -> Qubit 1 does not match Qubit 2, but 2 matches 3. 
        # Error is located at Qubit 0!
        elif syndrome == [0, 1]:
            print(" -> AI Syndrome Diagnosis: Gravity corrupted Qubit Index 0.")
            current_chain[0] = 1 - current_chain[0] # Apply Pauli-X flip simulation
            return current_chain, "CORRECTED_QUBIT_0"
        
        # Case 3: [0, 0] -> Qubit 1 differs from 2, and 2 differs from 3.
        # Error is located at the center link, Qubit 1!
        elif syndrome == [0, 0]:
            print(" -> AI Syndrome Diagnosis: Gravity corrupted Qubit Index 1.")
            current_chain[1] = 1 - current_chain[1] # Apply Pauli-X flip simulation
            return current_chain, "CORRECTED_QUBIT_1"

        # Case 4: [1, 0] -> Qubit 1 matches 2, but 2 differs from 3.
        # Error is located at Qubit 2!
        elif syndrome == [1, 0]:
            print(" -> AI Syndrome Diagnosis: Gravity corrupted Qubit Index 2.")
            current_chain[2] = 1 - current_chain[2] # Apply Pauli-X flip simulation
            return current_chain, "CORRECTED_QUBIT_2"
        
def run_quantum_chain_simulation():
    print("=" * 65)
    print("   PHASE 6: 3-QUBIT ENTANGLED CHAIN INTERFACE")
    print("=" * 65)
    time.sleep(1)

    # Initialize a clean logical state [0, 0, 0] across three entangled physical qubits
    quantum_chain = [0, 0, 0]
    agent = AdvancedQuantumAgent()

    print(f"[SYSTEM] Entangled Quantum Chain Initialised: {quantum_chain}")
    print("[SYSTEM] Syndrome measurement matrices active on AI dashboard.")
    print("-" * 65)
    time.sleep(1.5)

    # Simulating 5 deep descent iterations toward the singularity core
    for step in range(1, 6):
        print(f"\nStep {step:02d}: Quantum Chain Depth = {step * 1000} Planck Units")
        time.sleep(0.5)

        # Environmental Phase: Gravity attempts to destroy one random qubit in our chain
        if random.random() < 0.6:  # 60% chance of extreme gravitational noise interference
            corrupted_index = random.randint(0, 2)
            quantum_chain[corrupted_index] = 1 - quantum_chain[corrupted_index] # Inject bit-flip
            print(f"[ALERT] Gravitational flux struck the chain! State scrambled.")
        else:
            print("[INFO] Spacetime background stable. Matrix integrity holding.")

        print(f" -> Telemetry State (Pre-Correction): {quantum_chain}")

        # AI Phase: The Agent runs an indirect syndrome check
        syndrome = agent.measure_syndrome(quantum_chain)
        print(f" -> AI Syndrome Signature Readout: {syndrome}")
        time.sleep(1)

        # The Agent applies the correction matrix based on the signature
        quantum_chain, outcome = agent.execute_error_correction(quantum_chain, syndrome)

        if outcome != "NO_ERROR":
            print(f" -> Action: Pauli-X Correction Matrix deployed to target node.")
            print(f" -> Telemetry State (Post-Correction): {quantum_chain} [HEALED]")
        else:
            print(" -> Action: No corrective action required. Data fidelity is 100%.")

        time.sleep(1)

    print("\n" + "=" * 65)
    print(" [SUCCESS] ENTANGLED CORE TELEMETRY TRANSITION COMPLETED")
    print("           Quantum information perfectly preserved through code.")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    run_quantum_chain_simulation()