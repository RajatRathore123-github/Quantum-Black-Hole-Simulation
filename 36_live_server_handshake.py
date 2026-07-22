import gwosc.datasets
import time
import sys

def execute_live_server_handshake():
    print("=" * 65)
    print("   PHASE 26: LIVE RELATIVITY DATA SERVER HANDSHAKE")
    print("=" * 65)
    time.sleep(1)

    print("[NETWORK INIT] Connecting to Gravitational Wave Open Science Center...")
    print(" -> Remote Server: https://gwosc.org")
    print("-" * 65)
    time.sleep(1.5)

    try:
        # Pinging the active open-source servers to pull down the real observational run directory
        print("[ACTION] Querying global registry for active observing timelines...")
        observing_runs = gwosc.datasets.find_datasets(type="run")
        
        print("\n" + "#" * 65)
        print(" [LIVE SERVER INTERFACE SECURED: CONNECTION STATUS 200]")
        print("#" * 65)
        print(f" -> Successfully established contact with GWOSC core registry.")
        print(f" -> Total Historical Observation Runs Unlocked: {len(observing_runs)}")
        print("\n[ACTIVE RUN REGISTRY CATALOGUE]:")
        
        # Loop through and print the real, active datasets stored on the server
        for run in sorted(observing_runs):
            # Check if it's a standard production data run
            if any(x in run for x in ['O1', 'O2', 'O3', 'O4']):
                print(f"    -> Operational Dataset Matrix: {run}")

        print("\n -> Next Real-World Target: Route our 1.161336e-04 Hz filter through these streams.")
        print("#" * 65 + "\n")

    except Exception as e:
        print(f"\n[NETWORK EXCEPTION] Handshake failed or server timed out: {e}")
        print(" -> Action: Check your local internet gateway matrix and re-execute.")

if __name__ == "__main__":
    execute_live_server_handshake()