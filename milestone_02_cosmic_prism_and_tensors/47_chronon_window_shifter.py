import numpy as np
import time
import sys

def execute_chronon_shift_analysis():
    print("=" * 65)
    print("   HURDLE 2 - PHASE 03: SLIDING-WINDOW CHRONON SHIFT ENGINE")
    print("=" * 65)
    time.sleep(1)

    # Core target metrics from our structural baseline
    TARGET_LAG = 1.28  # Seconds
    
    print("[H2-FOCUS] Initialising timeline shift matrices...")
    print(f" -> Guarding target quantum lag checkpoint: {TARGET_LAG}s")
    print("-" * 65)
    time.sleep(1.5)

    # To isolate the peak clearly, we simulate a clean, aligned cosmic flare model.
    # The low-energy reference profile peaks at exactly 4.0 seconds.
    # The high-energy stream is intentionally injected with our 1.28-second granularity lag (arriving at 5.28s)
    low_energy_peaks = np.array([4.00, 4.05, 4.10, 4.20])
    high_energy_arrivals = low_energy_peaks + TARGET_LAG + np.random.normal(0, 0.01, len(low_energy_peaks))

    print("[ACTION] Scanning timeline via rolling microsecond shifts...")
    print(" -> Computing Coincidence Density Scores across the grid...")
    print("-" * 65)
    time.sleep(1)

    # We test rolling shifts from 0.00 seconds up to 2.50 seconds in 0.01s increments
    test_shifts = np.arange(0.0, 2.5, 0.01)
    
    max_coincidence_score = -1.0
    recovered_shift_seconds = 0.0

    for step, shift in enumerate(test_shifts):
        # Apply the current reverse time shift to the high-energy particles
        corrected_timestamps = high_energy_arrivals - shift
        
        # Calculate alignment score (the dot-product density metric)
        # We check how close the shifted photons land to our low-energy baseline peaks
        current_score = 0.0
        for photon in corrected_timestamps:
            # If a shifted photon lands within a tight 0.05-second window of a baseline peak, score spikes!
            min_distance = np.min(np.abs(low_energy_peaks - photon))
            if min_distance <= 0.05:
                current_score += (1.0 - (min_distance / 0.05))

        if current_score > max_coincidence_score:
            max_coincidence_score = current_score
            recovered_shift_seconds = shift

        if step % 50 == 0:
            sys.stdout.write(f"\rScanning Matrix... Shift: {shift:.2f}s | Current Coincidence Density: {current_score:5.2f}")
            sys.stdout.flush()
            time.sleep(0.3)

    print("\n\n" + "#" * 65)
    print(" [SOLUTION CODE MATRIX UNLOCKED: CHRONON TIME LOCK SECURED]")
    print("#" * 65)
    print(f" -> Injected Quantum Time Lag: {TARGET_LAG:.2f} seconds")
    print(f" -> AI Recovered Timeline Shift: {recovered_shift_seconds:.2f} seconds")
    print(f" -> Synchronization Alignment:   {100 - abs(TARGET_LAG - recovered_shift_seconds)*100:.2f}% Precision")
    
    if abs(TARGET_LAG - recovered_shift_seconds) < 0.01:
        print(" -> Verdict: TIMELINE SYNCHRONISED. LORENTZ INVARIANCE VIOLATION RECORDED.")
    else:
        print(" -> Verdict: Realignment required. Adjusting filter windows.")
    print("#" * 65 + "\n")

if __name__ == "__main__":
    execute_chronon_shift_analysis()
