import os
import sys
import time

def display_p2_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 75)
    print("      PROJECT 2: PARENT-TO-CHILD THERMODYNAMIC ENERGY LEAKAGE PORTAL")
    print("=" * 75)
    print(" [1] Execute Phase 01: Parent-to-Child Energy Influx Baseline Engine")
    print(" [2] Execute Phase 02: CMB Spherical Harmonics Anomaly Extractor")
    print(" [3] Execute Phase 03: Time-Varying Accretion Hubble Tension Solver")
    print(" [4] Execute Phase 04: Compile & Export Machine-Readable JSON Bounds")
    print(" [5] Execute Phase 05: Run Future Thermodynamic Entropy Gradient Loop")
    print("-" * 75)
    print(" [0] Return to Local System Command Prompt")
    print("=" * 75)

def main():
    while True:
        display_p2_menu()
        choice = input("Select a Dark Energy processing module to initialize: ").strip()
        
        if choice == '1': 
            os.system('python 53_dark_energy_leakage.py')
        elif choice == '2': 
            os.system('python 54_cmb_anomaly_filter.py')
        elif choice == '3': 
            os.system('python 55_tension_resolver.py')
        elif choice == '4': os.system('python 56_serialize_project2_bounds.py')
        elif choice == '5': os.system('python 57_entropy_gradient.py')
        elif choice == '6': os.system('python 58_build_project2_manuscript.py')
        elif choice == '0':
            print("\nLocking down Project 2 configurations. Data matrices archived safely.")
            break
        else:
            print("\nInvalid control selection. Retrying coordinate check...")
            
        input("\nPress Enter to return to the Project 2 Portal dashboard...")

if __name__ == "__main__":
    main()
