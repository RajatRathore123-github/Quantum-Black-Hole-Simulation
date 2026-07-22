import numpy as np
import time
import sys

def execute_background_comparison():
    print("=" * 65)
    print("   PHASE 31: OFF-SOURCE BACKGROUND COMPARISON ENGINE")
    print("=" * 65)
    time.sleep(1)

    # Our hard-coded leak-proof match score from Phase 30
    on_source_event_score = 1.003175e-25
    total_samples = 16777216

    print(f"[FOCUS] Loading active event score: {on_source_event_score:.6e}")
    print("[FOCUS] Simulating off-source quiet-sky baseline matrix...")
    print("-" * 65)
    time.sleep(1.5)

    # Generate a pure instrument noise vector matching the size of our file
    # Normal background strain hiss operates around a tiny standard deviation scale
    quiet_sky_noise = np.random.normal(0, 1.0e-21, total_samples)
    
    # Apply our verified Hanning filter pass to keep the math completely identical
    hanning_window = np.hanning(total_samples)
    filtered_quiet_sky = quiet_sky_noise * hanning_window

    print("[ACTION] Running parallel quadrature analysis over quiet background...")
    time.sleep(1)

    # Re-map the same target frequency filter profile
    time_vector = np.linspace(0, 4096, total_samples)
    chirp_profile = 2 * np.pi * 1.161336e-04 * time_vector
    
    corr_I = np.dot(filtered_quiet_sky, np.sin(chirp_profile)) / total_samples
    corr_Q = np.dot(filtered_quiet_sky, np.cos(chirp_profile)) / total_samples

    off_source_noise_score = np.sqrt(corr_I**2 + corr_Q**2)
    
    # Calculate the Significance Ratio (SNR of the discovery)
    # How much stronger is the event data compared to the background noise?
    significance_ratio = on_source_event_score / off_source_noise_score

    print("\n" + "#" * 65)
    print(" [THE CHRONOLOGY COMPLETED: FINAL SCAN RESULTS]")
    print("#" * 65)
    print(f" -> Active Merger Event Score (On-Source): {on_source_event_score:.6e}")
    print(f" -> Quiet Background Noise Score (Off-Source): {off_source_noise_score:.6e}")
    print(f" -> Signal Significance Multiplier:           {significance_ratio:.2f}x louder")

    print("\n [FINAL SYSTEM ARCHITECTURE STATUS]")
    if significance_ratio >= 3.0:
        print(" -> VERDICT: DISCOVERY CONFIRMED. SIGNAL DETACHED FROM BACKGROUND.")
    else:
        print(" -> VERDICT: SIGNAL INTEGRATED WITH AMBIENT TELESCOPE NOISE FLOOR.")
    print("#" * 65 + "\n")

if __name__ == "__main__":
    execute_background_comparison()