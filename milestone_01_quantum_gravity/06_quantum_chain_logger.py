import numpy as np
import time
import random
import os

class AdvancedQuantumAgent:
    def __init__(self):
        self.pauli_x = np.array([[0, 1], [1, 0]])

    def measure_syndrome(self, current_chain):
        syn_1_2 = 1 if current_chain[0] == current_chain[1] else 0
        syn_2_3 = 1 if current_chain[1] == current_chain[2] else 0
        return [syn_1_2, syn_2_3]

    def execute_error_correction(self, current_chain, syndrome):
        if syndrome == [1, 1]:
            return current_chain, "NO_ERROR", "Data fidelity is 100%"
        elif syndrome == [0, 1]:
            current_chain[0] = 1 - current_chain[0]
            return current_chain, "CORRECTED_QUBIT_0", "Gravity corrupted Qubit Index 0 -> Restored via Pauli-X"
        elif syndrome == [0, 0]:
            current_chain[1] = 1 - current_chain[1]
            return current_chain, "CORRECTED_QUBIT_1", "Gravity corrupted Qubit Index 1 -> Restored via Pauli-X"
        elif syndrome == [1, 0]:
            current_chain[2] = 1 - current_chain[2]
            return current_chain, "CORRECTED_QUBIT_2", "Gravity corrupted Qubit Index 2 -> Restored via Pauli-X"
        return current_chain, "UNKNOWN_STATE", "Unknown anomaly detected"
    
def run_logged_simulation():
    # Define our output file name
    log_filename = "quantum_telemetry_report.txt"
    
    # We open a clean text file to write our research logs
    with open(log_filename, "w", encoding="utf-8") as log_file:
        
        # Helper function to print to terminal AND write to the file simultaneously
        def log_write(text):
            print(text)
            log_file.write(text + "\n")

        log_write("=" * 65)
        log_write("   PHASE 7: MULTI-QUBIT CHAIN WITH TELEMETRY FILE EXPORTER")
        log_write("=" * 65)
        
        quantum_chain = [0, 0, 0]
        agent = AdvancedQuantumAgent()

        log_write(f"[SYSTEM] Entangled Quantum Chain Initialised: {quantum_chain}")
        log_write("[SYSTEM] Writing active data stream to local .txt matrix logs...")
        log_write("-" * 65)

        for step in range(1, 6):
            log_write(f"\nStep {step:02d}: Quantum Chain Depth = {step * 1000} Planck Units")

            if random.random() < 0.6:
                corrupted_index = random.randint(0, 2)
                quantum_chain[corrupted_index] = 1 - quantum_chain[corrupted_index]
                log_write(f"[ALERT] Gravitational flux struck the chain! State scrambled.")
            else:
                log_write("[INFO] Spacetime background stable. Matrix integrity holding.")

            log_write(f" -> Telemetry State (Pre-Correction): {quantum_chain}")

            syndrome = agent.measure_syndrome(quantum_chain)
            log_write(f" -> AI Syndrome Signature Readout: {syndrome}")

            quantum_chain, outcome, details = agent.execute_error_correction(quantum_chain, syndrome)
            log_write(f" -> AI Diagnosis & Action: {details}")
            log_write(f" -> Telemetry State (Post-Correction): {quantum_chain}")

        log_write("\n" + "=" * 65)
        log_write(" [SUCCESS] TRANSLATION ENDED: REPORT GENERATED")
        log_write("=" * 65 + "\n")

    print(f"\n[FILE EXPORTED] Verification check: Check file '{log_filename}' in your directory.")

if __name__ == "__main__":
    run_logged_simulation()