import numpy as np
import time

def simulate_real_quantum_gates():
    print("=" * 65)
    print("   PHASE 9: INTRODUCING HADAMARD & CNOT MATRIX OPERATIONS")
    print("=" * 65)
    time.sleep(1)

    # --- DEFINE THE QUANTUM GATES AS MATHEMATICAL MATRICES ---
    # The Hadamard Matrix: Creates superposition
    H_gate = (1 / np.sqrt(2)) * np.array([[1, 1],
                                          [1, -1]])

    # The CNOT Matrix: A 4x4 matrix that entangles two qubits
    # It leaves states 00 and 01 alone, but flips 10 to 11 and 11 to 10.
    CNOT_gate = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ])
    
    print("[SYSTEM] Quantum gate operator matrices compiled.")
    print(" -> Hadamard (H) Matrix initialized (2x2).")
    print(" -> Controlled-NOT (CNOT) Matrix initialized (4x4).")
    print("-" * 65)
    time.sleep(1.5)

    # --- STEP 1: INITIAL STATE PREPARATION ---
    # We start with a single clean qubit in state |0>
    qubit_0 = np.array([1, 0])
    print(f"Initial Qubit 0 State Vector: {qubit_0} (Definitive 0)")
    time.sleep(1)

    # --- STEP 2: APPLY THE HADAMARD ROTATION ---
    # Rotate the qubit using matrix multiplication to put it in superposition
    superposition_state = np.dot(H_gate, qubit_0)
    print(f"\n[ACTION] Applying Hadamard Gate to Qubit 0...")
    time.sleep(1)
    print(f" -> New State Vector Matrix: {superposition_state}")
    print(f" -> Mathematical Status: Perfect 50/50 Superposition blur.")
    print(f" -> Verification: amplitudes squared = {superposition_state[0]**2:.2f} + {superposition_state[1]**2:.2f} = 1.00")
    print("-" * 65)
    time.sleep(1.5)

    # --- STEP 3: CREATING ENTANGLEMENT (THE BELL STATE) ---
    print("[ACTION] Preparing multi-qubit system for CNOT entanglement...")
    time.sleep(1)

    # We create a combined 2-qubit state vector using a Kronecker tensor product.
    # Combining our superposition qubit with a second stable qubit |0> creates state:
    # 0.707*|00> + 0.0*|01> + 0.707*|10> + 0.0*|11>
    qubit_1 = np.array([1, 0])
    combined_system = np.kron(superposition_state, qubit_1)
    
    # Apply the 4x4 CNOT matrix to link their fates together
    entangled_bell_state = np.dot(CNOT_gate, combined_system)
    
    print("\n[SUCCESS] CNOT Matrix executed over combined system.")
    print(f" -> Final Entangled Bell State Vector:\n    {entangled_bell_state}")
    print("\n -> Analysis of the Core Matrix:")
    print(f"    Chance of measuring state |00> (Both stable): {entangled_bell_state[0]**2 * 100:.1f}%")
    print(f"    Chance of measuring state |11> (Both exploded): {entangled_bell_state[3]**2 * 100:.1f}%")
    print("    Chance of measuring mixed states (|01> or |10>): 0.0% [ENTANGLED]")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    simulate_real_quantum_gates()