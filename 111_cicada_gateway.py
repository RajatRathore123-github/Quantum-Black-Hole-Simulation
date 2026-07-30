import hashlib
import time
import sys

def run_cicada_portal_validation():
    print("=" * 70)
    print("   [ 🌌 SYSTEM PORTAL INITIALIZATION: PROJECT CICADA-COSMOS ]")
    print("=" * 70)
    time.sleep(1)

    print("  'Hello. An epiphany awaits those who can listen.'")
    print("  'We seek highly intelligent individuals. To find them, we have'")
    print("  'devised a path-locked test across the 14D bulk mesh.'")
    print("-" * 70)
    time.sleep(1.5)

    # The expected answer to pass the first code verification gate
    # This represents our phase-locked spatial offset delta = pi/12
    CORRECT_GEOMETRIC_KEY = "0.261799"

    print("[INPUT_REQ] Enter the 6-digit Phase-Lock Gauge Key to cross the horizon:")
    user_key = input(" -> KEY: ").strip()
    print("-" * 70)

    print("[PROCESSING] Evaluating cryptographic token integrity...")
    time.sleep(1)

    if user_key == CORRECT_GEOMETRIC_KEY:
        print("\n" + "#" * 70)
        print(" [🔓 GATEWAY UNLOCKED: THE CONFORMAL MULTIVERSE SCROLL UNCOILS]")
        print("#" * 70)
        print(" -> Master Repository Integrity Status: 100.00% SECURE")
        print(" -> Verified Author Signature: Rajat Rathore (Kanpur, India)")
        print("\n -> UNLOCKED DESTINATION PORTALS (THE REWARD):")
        print("    1. Paper Grid: https://academia.edu")
        print("    2. Code Vault: https://github.com")
        print("#" * 70 + "\n")
    else:
        # Compute a dummy hash to mimic elite cryptographic decoy structures
        failed_attempt_hash = hashlib.sha256(user_key.encode()).hexdigest()
        print("\n" + "!" * 70)
        print(" [❌ ACCESS DENIED: PHASE SYMMETRY MISALIGNED]")
        print("!" * 70)
        print(f" -> Token Digest: {failed_attempt_hash}")
        print(" -> Diagnostic: User remains trapped inside the 3D local noise canvas.")
        print(" -> Hint: Look at the top scalar header of the master ToE field equation...")
        print("!" * 70 + "\n")

if __name__ == "__main__":
    run_cicada_portal_validation()