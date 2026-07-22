from gwosc.locate import get_event_urls
import urllib.request
import h5py
import numpy as np
import os
import time

def execute_payload_extraction():
    print("=" * 65)
    print("   PHASE 28: DOWNLOADING & EXTRACTING LIVE EVENT PAYLOAD")
    print("=" * 65)
    time.sleep(1)

    event_name = "GW150914"
    detector = "H1"
    output_hdf5 = "gw150914_data.hdf5"
    output_npy = "gw150914_raw_strain.npy"

    print(f"[SYSTEM] Locating data stream for: {event_name}")
    print("-" * 65)
    time.sleep(1)

    try:
        # Step A: Fetch the real URL from the server
        urls = get_event_urls(event_name, detector=detector, sample_rate=4096)
        hdf5_urls = [u for u in urls if u.endswith('.hdf5')]
        
        if not hdf5_urls:
            print("[ERROR] No standard HDF5 target found on server.")
            return
            
        target_url = hdf5_urls[0]
        print(f"[SUCCESS] Remote target matched. Initiating secure stream...")

        # Step B: Download the raw file locally
        urllib.request.urlretrieve(target_url, output_hdf5)
        print(f" -> File secured: '{output_hdf5}' ({os.path.getsize(output_hdf5)/(1024*1024):.2f} MB)")
        print("-" * 65)
        time.sleep(1)

        # Step C: Open HDF5 and unpack the raw data matrix array
        print("[ACTION] Unpacking HDF5 groups and extracting raw strain vector...")
        with h5py.File(output_hdf5, 'r') as f:
            raw_strain = f['strain/Strain'][()]

        print(f" -> Successfully extracted matrix array. Shape: {raw_strain.shape}")

        # Step D: Save as a clean NumPy file for high-speed local processing
        np.save(output_npy, raw_strain)
        print(f" -> Array compiled and saved locally as: '{output_npy}'")
        
        print("\n" + "#" * 65)
        print(" [PAYLOAD EXTRACTION MATRIX LOCKED: DATA READY]")
        print("#" * 65)
        print(" -> Real event data is fully extracted and un-scrambled.")
        print(" -> Ready to deploy our 1.161336e-04 Hz echo matching matrix.")
        print("#" * 65 + "\n")

    except Exception as e:
        print(f"\n[NETWORK CRASH] Data download or extraction loop failed: {e}")

if __name__ == "__main__":
    execute_payload_extraction()