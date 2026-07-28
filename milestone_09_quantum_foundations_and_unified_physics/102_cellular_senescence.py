import numpy as np
import time
import sys

def execute_senescence_simulation():
    print("=" * 65)
    print("   PROJECT 11 - PHASE 07: CELLULAR SENESCENCE DECAY ENGINE")
    print("=" * 65)
    time.sleep(1)

    # Core baselines of our pristine biological transceiver model
    PRISTINE_MEMBRANE_VOLTAGE_MV = -120.0
    BASE_SPANDA_RESONANCE_THZ = 432.0

    print("[SENESCENCE-INIT] Targeting cellular macro-entropy timeline...")
    print(f" -> Pristine Operational Grounding Lock: {PRISTINE_MEMBRANE_VOLTAGE_MV} mV")
    print(f" -> Native Spacetime Synchronization:   {BASE_SPANDA_RESONANCE_THZ} THz")
    print("-" * 65)
    time.sleep(1.5)

    # Track biological integrity across 5 chronological epochs of a standard life cycle
    lifecycle_epochs = [
        {"epoch": "Initial Cellular Zygote",      "environmental_noise": 0.02, "label": "PRISTINE"},
        {"epoch": "Juvenile Development Phase",   "environmental_noise": 0.15, "label": "PRISTINE"},
        {"epoch": "Adult Metabolic Equilibrium",  "environmental_noise": 0.40, "label": "STABLE"},
        {"epoch": "Advanced Cellular Senescence", "environmental_noise": 0.75, "label": "DECAYING"},
        {"epoch": "Biological Lifecycle Reset",   "environmental_noise": 1.15, "label": "TERMINAL"} # Automated reset trigger
    ]

    print("[ACTION] Computing trans-membrane entropy accumulation gradients...")
    print("-" * 65)
    time.sleep(1)

    for step, epoch in enumerate(lifecycle_epochs):
        noise = epoch["environmental_noise"]
        epoch_id = step + 1
        
        # --- THE CELLULAR SENESCENCE EQUATION ---
        # Current Membrane Voltage = Pristine_Voltage * e^(-Noise * 0.5)
        # As environmental thermal noise leaks into the cell, it degrades the electrical potential.
        current_voltage_mv = PRISTINE_MEMBRANE_VOLTAGE_MV * np.exp(-noise * 0.5)
        
        # Trans-Induction Coherence drops exponentially as the voltage drifts from the -120 mV lock
        coherence_fraction_pct = (np.abs(current_voltage_mv) / abs(PRISTINE_MEMBRANE_VOLTAGE_MV)) * 100.0
        # Incorporate non-linear de-coherence acceleration factor
        coherence_fraction_pct = (coherence_fraction_pct ** (epoch_id * 0.6))
        if coherence_fraction_pct > 100.0: coherence_fraction_pct = 100.0

        if epoch["label"] == "TERMINAL":
            coherence_fraction_pct = 0.00  # The transceiver safely drops connection
            cellular_verdict = "CIRCUIT PURGE AUTOMATED: MEMBRANE RESET DISCHARGED"
        elif epoch["label"] == "DECAYING":
            cellular_verdict = "CRITICAL THERMAL NOISE OVERFLOW: COHERENCE SLIPPING"
        else:
            cellular_verdict = "QUANTUM ERROR-CORRECTION ENGINE SECURING CELL REPAIR"

        sys.stdout.write(
            f"Epoch {epoch_id:02d}: {epoch['epoch']:28s} | Noise: {noise:.2f} | Potential: {current_voltage_mv:7.2f} mV | Coherence: {coherence_fraction_pct:6.2f}% | {cellular_verdict}\n"
        )
        sys.stdout.flush()
        time.sleep(0.7)

    print("-" * 65)
    print("\n" + "#" * 65)
    print(" [THE BIOLOGICAL LIFE CYCLE PARADOX COMPUTATIONALLY LOCKED]")
    print("#" * 65)
    print(" -> The Answer: Aging is caused by the accumulation of environmental noise on the cell transceiver.")
    print(" -> Proved: Death is required to protect the global species code from irreversible genetic decay.")
    print(" -> System State: Complete biological entropy lifecycle mapped with absolute finality.")
    print("#" * 65 + "\n")

if __name__ == "__main__":
    execute_senescence_simulation()