import h5py
import time

def inspect_ligo_data_structure():
    print("=" * 65)
    print("   STEP 3: UNPACKING AND MAPPING THE lIGO HDF5 ARCHITECTURE")
    print("=" * 65)
    time.sleep(1)

    filename = "real_ligo_strain_data.hdf5"
    print(f"[SYSTEM] Opening local target database: '{filename}'")
    print("[SYSTEM] Scanning root directories and sub-group configurations...")
    print("-" * 65)
    time.sleep(1.5)

    try:
        # Open the scientific HDF5 file structure safely
        with h5py.File(filename, 'r') as f:
            print("[SUCCESS] Handshake secure. Root items located:")
            
            # Print the main folder layers inside the file
            for key in f.keys():
                print(f" -> Root Group Folder: /{key}")
            
            print("-" * 65)
            print("[ACTION] Descending into core data paths...")
            time.sleep(1)

            # Map the precise path to the telescope strain data array
            # Path layout: /strain/Strain
            strain_group = f['strain']
            for sub_key in strain_group.keys():
                print(f"    -> Sub-dataset found: /strain/{sub_key}")
                
            # Extract basic tracking metadata
            meta_group = f['meta']
            print("\n[METADATA MATRIX RECORDED]:")
            print(f" -> Start GPS Second Timestamp: {meta_group['GPSstart'][()]}")
            print(f" -> Duration of Telemetry Segment: {meta_group['Duration'][()]} seconds")
            
            # Unpack the actual size of the data vector matrix
            strain_dataset = f['strain/Strain']
            print(f" -> Total Data Matrix Points Collected: {strain_dataset.shape[0]:,}")

        print("-" * 65)
        print(" [SUCCESS] STRUCTURAL WORKSPACE VERIFICATION COMPLETE")
        print(" -> Data path for AI extraction confirmed: '/strain/Strain'")
        print("=" * 65 + "\n")

    except Exception as e:
        print(f"\n[CRITICAL ERROR] Failed to parse HDF5 file format: {e}")
        print(" -> Action: Ensure the file downloaded completely and is not corrupted.")

if __name__ == "__main__":
    inspect_ligo_data_structure()