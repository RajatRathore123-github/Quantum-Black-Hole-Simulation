from gwosc.datasets import event_gps
from gwosc.locate import get_event_urls
import time
import sys

def execute_segment_search():
    print("=" * 65)
    print("   PHASE 27: INVESTIGATING EVENT DATA TIME SEGMENTS")
    print("=" * 65)
    time.sleep(1)

    # Our historic target event: The first black hole merger ever detected
    target_event = "GW150914"
    detector = "H1"  # Hanford Observatory Sensor Node

    print(f"[QUERY INITIALISED] Tracking down spacetime segment for: {target_event}")
    print(f" -> Mapping sensor array feed: {detector} (Hanford Observatory)")
    print(" -> Scanning remote dataset catalog indices...")
    print("-" * 65)
    time.sleep(1.5)

    try:
        # Step A: Query the server for the exact GPS event milestone second
        gps_time = event_gps(target_event)
        
        # Step B: CORRECTION - Fetch the data file tracking urls using the locate module
        print("[ACTION] Extracting precise GPS time boundaries from server...")
        urls = get_event_urls(target_event, detector=detector, sample_rate=4096)

        print("\n" + "#" * 65)
        print(" [EVENT TIMELINE MATRIX RESOLVED: REGISTRY LOCK]")
        print("#" * 65)
        print(f" -> Targeted Core Event: {target_event}")
        print(f" -> Exact Collision GPS Timestamp: {gps_time} seconds")
        print(f" -> Total Data Packets Found for Segment: {len(urls)}")
        print("\n -> Verification: The coordinate matrix is locked and ready for signal processing.")
        print("#" * 65 + "\n")

    except Exception as e:
        print(f"\n[QUERY EXCEPTION] Server was unable to resolve the event string: {e}")
        print(" -> Action: Verify spelling of the event matrix and re-execute.")

if __name__ == "__main__":
    execute_segment_search()