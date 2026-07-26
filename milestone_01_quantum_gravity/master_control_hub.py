import os
import sys

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 75)
    print("      QUANTUM BLACK HOLE RESEARCH SIMULATION & OBSERVATIONAL HUB")
    print("=" * 75)
    print(" [1-9] Run Core Simulation Phases (Relativity, Agents, Quantum Gates)")
    print(" [A-C] Run Theoretical Solution Core (Phase Transition, Unified Field)")
    print("-" * 75)
    print(" [H1]  THE COMPLETED HURDLE 1 OPTICAL SCANNING BACKEND")
    print("       -> 13: Echo Predictor        | 23: Displacement Memory")
    print("       -> 24: Phase Stacker Matrix  | 32: Quantum Demodulator")
    print("       -> 33: Coherence Stabiliser  | 34: Dispersion Compensator")
    print("       -> 35: Pattern Data Matcher  | 36-39: Live GWOSC Server Miner")
    print("       -> 40: Spectral Window Pass  | 41: Off-Source Noise Auditor")
    print("-" * 75)
    print(" [DOC] COMPILATION, ARCHIVING, & ARXIV MANUSCRIPT INTERFACE")
    print("       -> [D1] Serialize JSON Parameter Vault")
    print("       -> [D2] Generate Academic Manuscript Draft Text")
    print(" [0]   Terminate Research Session")
    print("=" * 75)

def main():
    while True:
        display_menu()
        choice = input("Select a workspace console action: ").strip().upper()
        
        if choice in ['1','2','3','4','5','6','7','8','9']:
            cmds = {
                '1':'01_gravity_breakdown.py', '2':'02_quantum_interceptor.py',
                '3':'03_visual_bounce_plot.py', '4':'04_agentic_quantum_mitigation.py',
                '5':'05_three_qubit_quantum_chain.py', '6':'06_quantum_chain_logger.py',
                '7':'07_shor_nine_qubit_core.py', '8':'08_quantum_gate_rotations.py',
                '9':'09_asynchronous_quantum_core.py'
            }
            os.system(f"python {cmds[choice]}")
        elif choice == 'A': os.system('python 10_spacetime_phase_transition.py')
        elif choice == 'B': os.system('python 11_geometric_tunneling.py')
        elif choice == 'C': os.system('python 12_unified_pressure_tensor.py')
        elif choice == 'H1':
            print("\n    --- Active Hurdle 1 Repository Catalogue ---")
            print("    [13] Base Echoes       [23] Space Memory     [24] Phase Stacker")
            print("    [32] Demodulator      [33] Coherence Comb   [34] Dispersion Fix")
            print("    [35] Data Matcher     [36] Live Handshake   [37] Segment Finder")
            print("    [38] Payload Pull     [39] Raw Quad Match   [40] Spectral Window")
            print("    [41] Noise Auditor")
            sub = input("\n    Execute script script code (e.g. 34): ").strip()
            maps = {
                '13':'13_gravitational_echoes.py', '23':'23_spacetime_memory.py', '24':'24_quantum_phase_stacker.py',
                '32':'32_optical_demodulator.py', '33':'33_injection_locked_comb.py', '34':'34_dispersion_compensation.py',
                '35':'35_real_data_matcher.py', '36':'36_live_server_handshake.py', '37':'37_segment_finder.py',
                '38':'38_payload_extractor.py', '39':'39_real_data_quadrature_matcher.py', '40':'40_spectral_window_filter.py',
                '41':'41_background_comparison.py'
            }
            if sub in maps: os.system(f"python {maps[sub]}")
        elif choice == 'D1': os.system('python 43_blueprint_serializer.py')
        elif choice == 'D2': os.system('python 44_manuscript_builder.py')
        elif choice == '0':
            print("\nShutting down workspace control console. Core locked.")
            break
        else:
            print("\nInvalid control code signature matrix.")
            
        input("\nPress Enter to return to the Control Hub dashboard...")


if __name__ == "__main__":
    main()

