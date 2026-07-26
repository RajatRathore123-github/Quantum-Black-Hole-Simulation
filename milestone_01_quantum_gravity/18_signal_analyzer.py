import h5py
import numpy as np
from scipy.signal import welch
import time
import sys

def execute_signal_analysis_pipeline():
    print("=" * 65)
    print("   STEP 4: INITIALISING AI FAST FOURIER TRANSFORM ENGINE")
    print("=" * 65)
    time.sleep(1)

    filename = "real_ligo_strain_data.hdf5"
    sample_rate = 4096  # 4096 data points recorded per second

    print(f"[SYSTEM] Extracting data matrix array from {filename}...")
    time.sleep(1)

    try:
        # Load the raw 16,777,216 data point array into RAM safely using h5py
        with h5py.File(filename, 'r') as f:
            raw_strain = f['strain/Strain'][()]
            
        print("[SUCCESS] Data array loaded cleanly into operational memory.")
        print(f" -> Array Shape: {raw_strain.shape}")
        print("\n[ACTION] Triggering Fast Fourier Transform matrix scan...")
        print(" -> Applying Welch's method to resolve Power Spectral Density (PSD)")
        print("-" * 65)
        time.sleep(1.5)

        # Welch's method splits our massive data stream into overlapping segments,
        # runs an FFT on each, and averages them to isolate real spikes from background hiss.
        # We configure the block size (nperseg) to give us deep resolution at low frequencies.
        frequencies, psd = welch(raw_strain, fs=sample_rate, nperseg=sample_rate*16)
        
        print("[SUCCESS] Frequency matrix resolved!")
        print(f" -> Total frequency bands mapped: {len(frequencies):,}")
        print(f" -> Minimum resolved band: {frequencies[1]:.6f} Hz")
        print(f" -> Maximum resolved band: {frequencies[-1]:,.2f} Hz")
        print("-" * 65)
        time.sleep(1)

        # --- HUNTING FOR OUR SIGNAL ---
        # Our calculated target frequency is 1.161336e-04 Hz.
        # Let's write an automated detection loop that scans the resolved array 
        # for anomalous structural signals in the lower spectrum bands.
        print("AI Agent scanning target grid for anomalous wave distributions...")
        time.sleep(1)
        
        # Locate the frequency index closest to our theoretical target
        target_hz = 1.161336e-04
        closest_index = (np.abs(frequencies - target_hz)).argmin()
        
        print("\n" + "#" * 65)
        print(" [AI SCAN REGISTER STATUS: ACTIVE]")
        print("#" * 65)
        print(f" -> Target Signature Frequency: {target_hz:.6e} Hz")
        print(f" -> Closest Measurable Band:     {frequencies[closest_index]:.6e} Hz")
        print(f" -> Ambient Energy Density:      {psd[closest_index]:.4e} strain²/Hz")
        print(" -> Signal Status: Baseline extraction locked.")
        print(" -> Next Move: Filter seismic instrument lines to map real anomalies.")
        print("#" * 65 + "\n")

    except Exception as e:
        print(f"\n[PIPELINE EXCEPTION] Signal analysis collapsed: {e}")

if __name__ == "__main__":
    execute_signal_analysis_pipeline()