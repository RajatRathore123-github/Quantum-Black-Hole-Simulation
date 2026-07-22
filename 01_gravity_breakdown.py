import math

def calculate_cosmic_boundaries():
    print("=" * 60)
    print("  PHASE 1: CALCULATING THE RELATIVITY BREAK-DOWN POINT")
    print("=" * 60)

    # --- THE PHYSICAL CONSTANTS ---
    # These are the fixed rules of our universe.
    G = 6.6743e-11      # Gravitational Constant: How strong gravity pulls
    c = 299792458       # Speed of light in meters per second
    SOLAR_MASS = 1.989e30 # Mass of our Sun in kilograms

    # --- OUR TARGET: SAGITTARIUS A* ---
    # The black hole at the center of the Milky Way is 4.1 million times heavier than our sun.
    bh_mass_solar = 4100000
    bh_mass_kg = bh_mass_solar * SOLAR_MASS

    print(f"[!] Target: Sagittarius A*")
    print(f"    Mass: {bh_mass_solar:,} Solar Masses ({bh_mass_kg:.2e} kg)")
    print("-" * 60)

    # --- STEP 1: CALCULATE THE EVENT HORIZON ---
    # Formula: R_s = 2GM / c^2
    # This is Einstein's equation for the radius of a black hole.
    event_horizon_m = (2 * G * bh_mass_kg) / (c ** 2)
    event_horizon_km = event_horizon_m / 1000

    print(f"[SUCCESS] Event Horizon Calculated:")
    print(f"    Radius: {event_horizon_km:,.2f} km")
    print(f"    -> Inside this radius, gravity is stronger than light.")
    print("-" * 60)

    # --- STEP 2: CALCULATE THE PLANCK CORE LIMIT ---
    # The Planck Length is the absolute smallest size allowed by Quantum Physics (1.616e-35 meters)
    planck_length = 1.616255e-35
    
    print(f"[WARNING] Quantum Boundary (The Planck Floor):")
    print(f"    Radius: {planck_length:.2e} meters")
    print(f"    -> This is where Einstein's smooth space fabric breaks.")
    print("-" * 60)

    # --- STEP 3: THE MATHEMATICAL COLLAPSE ---
    # Let's show what happens to density as matter gets crushed down to 0 meters.
    print("Simulating density calculation as radius approaches zero:")
    
    test_radii = [1000, 1, 1e-10, 1e-30, 0] # Shrinking down to zero
    
    for r in test_radii:
        try:
            # Volume of a sphere: 4/3 * pi * r^3
            volume = (4/3) * math.pi * (r ** 3)
            # Density: Mass / Volume
            density = bh_mass_kg / volume
            print(f"    At Radius {r:10.0e} m -> Density is {density:.2e} kg/m³")
        except ZeroDivisionError:
            # This is the exact mathematical glitch we are going to solve!
            print(f"    At Radius {r:10.0e} m -> ERROR: Divided by Zero! Density is INFINITE.")

    print("=" * 60)

if __name__ == "__main__":
    calculate_cosmic_boundaries()