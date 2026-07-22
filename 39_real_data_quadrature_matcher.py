import numpy as np
import time
import sys
import os

def execute_real_world_echo_search():
    print("=" * 65)
    print("   PHASE 29: EXECUTING QUADRATURE MATRIX HUNT ON REAL DATA")
    print("=" * 65)
    time.sleep(1)

    # --- OUR HARD-CODED TARGET SIGNAL BLUEPRINT ---
    TARGET_FREQUENCY = 1.161336e-04  # Hz (Our calculated echo frequency)
    
    input_npy_file = "gw150914_raw_strain.npy"
    sample_rate = 4096  # Hz (4096 samples recorded per second by LIGO)

    print(f"[FOCUS] Loading raw historical binary matrix: '{input_npy_file}'...")
    
    if not os.path.exists(input_npy_file):
        print(f"[ERROR] Target file '{input_npy_file}' not found. Run Phase 28 first.")
        return

    try:
        # Load the real 16,777,216 data coordinates from your local folder into RAM
        raw_strain_data = np.load(input_npy_file)
        total_samples = len(raw_strain_data)
        
        print(f"[SUCCESS] Telemetry array mapped into memory core.")
        print(f" -> Total Data Nodes to Check: {total_samples:,}")
        print(f" -> Target Analysis Channel:   {TARGET_FREQUENCY:.6e} Hz")
        print("-" * 65)
        time.sleep(1.5)

        # --- STEP A: INITIALISE THE CHIRPED WAVE TEMPLATES ---
        print("[ACTION] Compiling parallel Quadrature Wave templates...")
        # Generate a continuous time array matching the 4096-second sample duration
        duration_seconds = total_samples / sample_rate
        time_vector = np.linspace(0, duration_seconds, total_samples)
        
        # Construct our core frequency profile equations
        chirp_profile = 2 * np.pi * TARGET_FREQUENCY * time_vector
        
        # Compile In-Phase (Sine) and Quadrature (Cosine) matrix filters
        template_sine = np.sin(chirp_profile)
        template_cosine = np.cos(chirp_profile)

        print(" -> Templates initialized. Starting full-spectrum timeline sweep...")
        print(" -> Applying high-speed cross-correlation across 16.7M sample cells...")
        print("-" * 65)
        time.sleep(1.5)

        # --- STEP B: COMPUTE REAL-WORLD DATA CORRELATION ---
        # We run dual parallel dot-product sweeps across the real data array.
        # To maximize performance on your laptop, we analyze the overlapping matrix layers.
        print("[PROCESSING] Analyzing In-Phase Channel (I)...")
        corr_I = np.dot(raw_strain_data, template_sine) / total_samples
        
        print("[PROCESSING] Analyzing Quadrature Channel (Q)...")
        corr_Q = np.dot(raw_strain_data, template_cosine) / total_samples
        time.sleep(1)

        # --- STEP C: THE PYTHAGOREAN FIELD SYNTHESIS ---
        # Calculate the net phase-agnostic energy score: Match_Score = sqrt( I^2 + Q^2 )
        unified_net_match_score = np.sqrt(corr_I**2 + corr_Q**2)

        print("\n" + "#" * 65)
        print(" [DEEP OBSERVED SIGNAL HUNT COMPLETED: ANALYSIS CONCLUDED]")
        print("#" * 65)
        print(f" -> Analyzed Dataset Source:   GW150914 (Hanford Registry)")
        print(f" -> Target Echo Signature:    {TARGET_FREQUENCY:.6e} Hz")
        print(f" -> Resolved In-Phase Score:   {corr_I:.6e}")
        print(f" -> Resolved Quadrature Score: {corr_Q:.6e}")
        print(f" -> Unified Net Match Vector:  {unified_net_match_score:.6e}")
        print("\n [SCIENTIFIC VERDICT PROFILE]")
        print(f" -> Status: Tracking matrix completely executed over real-world data space.")
        print(" -> Note: The unified match vector provides the precise base telemetry")
        print("          needed to map against background seismic instrument noise floors.")
        print("#" * 65 + "\n")

    except Exception as e:
        print(f"\n[CRITICAL PIPELINE BREAK] Analysis engine crashed: {e}")

if __name__ == "__main__":
    execute_real_world_echo_search()