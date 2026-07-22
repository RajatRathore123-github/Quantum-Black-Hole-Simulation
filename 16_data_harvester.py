from gwosc.locate import get_event_urls
import urllib.request
import os
import time

def harvest_real_ligo_data():
    print("=" * 65)
    print("   STEP 2: HARVESTING REAL-WORLD HISTORICAL lIGO STRAIN DATA")
    print("=" * 65)
    time.sleep(1)

    # --- THE ASTROPHYSICAL EVENT TARGET ---
    # GW170814: A definitive binary black hole merger event
    event_name = "GW170814"
    detector = "H1"  # H1 represents the LIGO observatory in Hanford, Washington

    print(f"[SYSTEM] Pinging Gravitational Wave Open Science Center servers...")
    print(f" -> Searching for data logs linked to target event: {event_name}")
    print(f" -> Mapping sensor array feed: {detector} (Hanford Observatory)")
    print("-" * 65)
    time.sleep(1.5)

    try:
        # CORRECTION: We use get_event_urls specifically for named events
        urls = get_event_urls(event_name, detector=detector, sample_rate=4096)
        
        # Filter URLs to find the standard HDF5 file configuration
        hdf5_urls = [u for u in urls if u.endswith('.hdf5')]
        
        if not hdf5_urls:
            print("[ERROR] Server responded, but no HDF5 file matrix was located.")
            return
        
        target_url = hdf5_urls[0]
        output_filename = "real_ligo_strain_data.hdf5"
        
        print("[SUCCESS] Data packet located on global registry server!")
        print(f" -> Remote URL: {target_url[:70]}...")
        print(f" -> Local destination: {output_filename}")
        print("\n[DOWNLOAD INIT] Pulling real cosmic wave data stream down to laptop...")
        
        # Downloading the real file from the scientific server straight into your folder
        urllib.request.urlretrieve(target_url, output_filename)
        
        print("-" * 65)
        print(" [SUCCESS] DATA PACKET SECURED LOCALLY")
        print(f" -> File saved cleanly as: '{output_filename}'")
        print(f" -> File size: {os.path.getsize(output_filename) / (1024*1024):.2f} MB")
        print("=" * 65 + "\n")

    except Exception as e:
        print(f"\n[CONNECTION ERROR] Server handshake failed or timed out: {e}")
        print(" -> Action: Check your internet connection matrix and re-execute.")

if __name__ == "__main__":
    harvest_real_ligo_data()