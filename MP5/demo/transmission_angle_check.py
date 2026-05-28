"""
MiniClaw Transmission Angle Check — Live MCP Tool Call Demo
Team Ricciotti-Berhe-Tesfatsion | MP5

Demonstrates a real engineering question: what happens to the transmission
angle when you change a link length? This is the kind of check the team
runs before committing to a geometry.

Usage:
    python3 transmission_angle_check.py
"""

import numpy as np


def compute_transmission_angle(L1, L2, L3, L4, O4_x, theta_min=-50, theta_max=50, n_points=200):
    """
    Compute transmission angle across the input range for a four-bar linkage.

    Parameters:
        L1: ground link length (mm)
        L2: input crank length (mm)
        L3: coupler length (mm)
        L4: output link length (mm)
        O4_x: x-offset of output pivot from input pivot (mm)
        theta_min, theta_max: input angle range (degrees)

    Returns:
        dict with mu_min, mu_max, margin_above_floor, in_band, thetas, mus
    """
    O2 = np.array([0.0, 0.0])
    O4 = np.array([O4_x, 0.0])

    thetas = np.linspace(theta_min, theta_max, n_points)
    mus = []

    for theta_deg in thetas:
        theta = np.radians(theta_deg)
        A = O2 + L2 * np.array([np.cos(theta), np.sin(theta)])

        dx = O4[0] - A[0]
        dy = O4[1] - A[1]
        d = np.sqrt(dx**2 + dy**2)

        if d > L3 + L4 or d < abs(L3 - L4):
            mus.append(np.nan)
            continue

        cos_mu = (L3**2 + L4**2 - d**2) / (2 * L3 * L4)
        cos_mu = np.clip(cos_mu, -1, 1)
        mu = np.degrees(np.arccos(cos_mu))
        mus.append(mu)

    mus = np.array(mus)
    valid = mus[~np.isnan(mus)]

    if len(valid) == 0:
        return {'error': 'No valid configurations in the given range'}

    mu_min = np.min(valid)
    mu_max = np.max(valid)
    margin = mu_min - 40.0
    in_band = mu_min >= 40.0 and mu_max <= 140.0

    return {
        'mu_min': mu_min,
        'mu_max': mu_max,
        'margin_above_floor': margin,
        'in_band': in_band,
        'thetas': thetas,
        'mus': mus
    }


def compute_jaw_opening(L1, L2, L3, L4, O4_pos, tip_ext=9.0, theta_min=-50, theta_max=50):
    """Compute max single-side displacement and total jaw opening."""
    O2 = np.array([0.0, 0.0])
    if isinstance(O4_pos, (list, tuple)):
        O4 = np.array(O4_pos, dtype=float)
    else:
        O4 = np.array([O4_pos, 0.0])

    ref_theta = np.radians(0)
    A_ref = O2 + L2 * np.array([np.cos(ref_theta), np.sin(ref_theta)])
    dx_ref = O4[0] - A_ref[0]
    dy_ref = O4[1] - A_ref[1]
    d_ref = np.sqrt(dx_ref**2 + dy_ref**2)
    cos_a = (L3**2 + d_ref**2 - L4**2) / (2 * L3 * d_ref)
    cos_a = np.clip(cos_a, -1, 1)
    alpha = np.arccos(cos_a)
    base = np.arctan2(dy_ref, dx_ref)
    theta3_ref = base - alpha
    B_ref = A_ref + L3 * np.array([np.cos(theta3_ref), np.sin(theta3_ref)])
    coupler_dir = (B_ref - A_ref) / np.linalg.norm(B_ref - A_ref)
    tip_ref = B_ref + tip_ext * coupler_dir

    max_disp = 0
    for theta_deg in np.linspace(theta_min, theta_max, 200):
        theta = np.radians(theta_deg)
        A = O2 + L2 * np.array([np.cos(theta), np.sin(theta)])
        dx = O4[0] - A[0]
        dy = O4[1] - A[1]
        d = np.sqrt(dx**2 + dy**2)
        if d > L3 + L4 or d < abs(L3 - L4):
            continue
        cos_a = (L3**2 + d**2 - L4**2) / (2 * L3 * d)
        cos_a = np.clip(cos_a, -1, 1)
        alpha = np.arccos(cos_a)
        base = np.arctan2(dy, dx)
        theta3 = base - alpha
        B = A + L3 * np.array([np.cos(theta3), np.sin(theta3)])
        c_dir = (B - A) / np.linalg.norm(B - A)
        tip = B + tip_ext * c_dir
        disp = np.linalg.norm(tip - tip_ref)
        max_disp = max(max_disp, disp)

    return {'max_single_side': max_disp, 'total_jaw_opening': 2 * max_disp}


if __name__ == '__main__':
    print("=" * 60)
    print("MiniClaw Transmission Angle Check — Live Demo")
    print("=" * 60)

    # Our chosen design
    print("\n--- Haben's design (chosen) ---")
    r = compute_transmission_angle(L1=47, L2=20, L3=29, L4=23, O4_x=47)
    j = compute_jaw_opening(L1=47, L2=20, L3=29, L4=23, O4_pos=(47, 0))
    print(f"  μ range:     {r['mu_min']:.1f}° – {r['mu_max']:.1f}°")
    print(f"  Margin:      {r['margin_above_floor']:.1f}° above 40° floor")
    print(f"  In band:     {'YES' if r['in_band'] else 'NO'}")
    print(f"  Jaw opening: {j['total_jaw_opening']:.2f} mm")

    # Perturbed geometry — what if L3 changes?
    print("\n--- Perturbed: L3 = 32 mm (was 29) ---")
    r2 = compute_transmission_angle(L1=47, L2=20, L3=32, L4=23, O4_x=47)
    j2 = compute_jaw_opening(L1=47, L2=20, L3=32, L4=23, O4_pos=(47, 0))
    print(f"  μ range:     {r2['mu_min']:.1f}° – {r2['mu_max']:.1f}°")
    print(f"  Margin:      {r2['margin_above_floor']:.1f}° above 40° floor")
    print(f"  In band:     {'YES' if r2['in_band'] else 'NO'}")
    print(f"  Jaw opening: {j2['total_jaw_opening']:.2f} mm")

    # David's design for comparison
    print("\n--- David's design (not selected) ---")
    r3 = compute_transmission_angle(L1=12, L2=26, L3=12, L4=26, O4_x=0,
                                     theta_min=0, theta_max=28)
    j3 = compute_jaw_opening(L1=12, L2=26, L3=12, L4=26, O4_pos=(0, 12), tip_ext=22,
                              theta_min=0, theta_max=28)
    print(f"  μ range:     {r3['mu_min']:.1f}° – {r3['mu_max']:.1f}°")
    print(f"  Margin:      {r3['margin_above_floor']:.1f}° above 40° floor")
    print(f"  In band:     {'YES' if r3['in_band'] else 'NO'}")
    print(f"  Jaw opening: {j3['total_jaw_opening']:.2f} mm")

    print("\n" + "=" * 60)
    print("Key takeaway: Changing L3 by just 3 mm shifts the")
    print("transmission angle band — the tool catches this instantly.")
    print("=" * 60)
