"""
MiniClaw Four-Bar Linkage Dynamic Simulation
Team Ricciotti-Berhe-Tesfatsion | MP5 Live Demo

Animates Haben's crossed-branch four-bar linkage sweeping from -50° to +50°,
showing jaw displacement and transmission angle in real time.

Usage:
    python3 linkage_simulation.py
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import FancyArrowPatch

# --- Linkage parameters (Haben's design) ---
L1 = 47.0   # ground link
L2 = 20.0   # input crank
L3 = 29.0   # coupler
L4 = 23.0   # output link
O2 = np.array([0.0, 0.0])     # input pivot (fixed)
O4 = np.array([47.0, 0.0])    # output pivot (fixed)
TIP_EXT = 9.0                  # tip extension past joint B

THETA_MIN = -50.0
THETA_MAX = 50.0
N_FRAMES = 200


def solve_four_bar(theta2_deg):
    """Solve the four-bar for a given input angle. Returns joint positions and mu."""
    theta2 = np.radians(theta2_deg)
    A = O2 + L2 * np.array([np.cos(theta2), np.sin(theta2)])

    dx = O4[0] - A[0]
    dy = O4[1] - A[1]
    d = np.sqrt(dx**2 + dy**2)

    if d > L3 + L4 or d < abs(L3 - L4):
        return None

    cos_alpha = (L3**2 + d**2 - L4**2) / (2 * L3 * d)
    cos_alpha = np.clip(cos_alpha, -1, 1)
    alpha = np.arccos(cos_alpha)

    base_angle = np.arctan2(dy, dx)
    theta3 = base_angle - alpha  # crossed branch

    B = A + L3 * np.array([np.cos(theta3), np.sin(theta3)])

    # Transmission angle
    cos_mu = (L3**2 + L4**2 - d**2) / (2 * L3 * L4)
    cos_mu_alt = (L3**2 + L4**2 - (dx**2 + dy**2)) / (2 * L3 * L4)
    cos_mu = np.clip(cos_mu, -1, 1)
    mu = np.degrees(np.arccos(cos_mu))

    # Tip position (extension past B along coupler direction)
    coupler_dir = (B - A) / np.linalg.norm(B - A)
    tip = B + TIP_EXT * coupler_dir

    return {
        'A': A, 'B': B, 'O2': O2, 'O4': O4, 'tip': tip,
        'mu': mu, 'theta2': theta2_deg
    }


def compute_displacement(result):
    """Compute single-side displacement from the reference (theta=0) position."""
    ref = solve_four_bar(0)
    if ref is None or result is None:
        return 0
    return np.linalg.norm(result['tip'] - ref['tip'])


# Pre-compute all frames
thetas = np.concatenate([
    np.linspace(THETA_MIN, THETA_MAX, N_FRAMES // 2),
    np.linspace(THETA_MAX, THETA_MIN, N_FRAMES // 2)
])

results = [solve_four_bar(t) for t in thetas]
displacements = [compute_displacement(r) for r in results]
mus = [r['mu'] if r else 0 for r in results]

# --- Set up figure ---
fig = plt.figure(figsize=(14, 7))
fig.suptitle('MiniClaw Four-Bar Linkage — Live Demo', fontsize=16, fontweight='bold')

ax_linkage = fig.add_subplot(121)
ax_data = fig.add_subplot(122)

ax_linkage.set_xlim(-15, 65)
ax_linkage.set_ylim(-35, 35)
ax_linkage.set_aspect('equal')
ax_linkage.set_xlabel('X (mm)')
ax_linkage.set_ylabel('Y (mm)')
ax_linkage.set_title('Linkage Motion')
ax_linkage.grid(True, alpha=0.3)

# Fixed pivots
ax_linkage.plot(*O2, 'ks', markersize=10, zorder=5, label='O2 (input)')
ax_linkage.plot(*O4, 'ks', markersize=10, zorder=5, label='O4 (output)')

# Moving elements (will be updated)
link_line, = ax_linkage.plot([], [], 'b-o', linewidth=2.5, markersize=6, zorder=4)
tip_marker, = ax_linkage.plot([], [], 'r^', markersize=12, zorder=5, label='Jaw tip')
tip_trail, = ax_linkage.plot([], [], 'r-', linewidth=0.8, alpha=0.4)
ground_line, = ax_linkage.plot([O2[0], O4[0]], [O2[1], O4[1]], 'k--', linewidth=1.5, alpha=0.5)

ax_linkage.legend(loc='upper left', fontsize=8)

# Data panel
ax_data.axis('off')
ax_data.set_xlim(0, 1)
ax_data.set_ylim(0, 1)

title_text = ax_data.text(0.5, 0.95, 'Real-Time Data', fontsize=14, fontweight='bold',
                          ha='center', va='top', transform=ax_data.transAxes)
theta_text = ax_data.text(0.1, 0.80, '', fontsize=13, transform=ax_data.transAxes,
                          family='monospace')
disp_text = ax_data.text(0.1, 0.68, '', fontsize=13, transform=ax_data.transAxes,
                         family='monospace')
jaw_text = ax_data.text(0.1, 0.56, '', fontsize=13, transform=ax_data.transAxes,
                        family='monospace', fontweight='bold', color='darkgreen')
mu_text = ax_data.text(0.1, 0.44, '', fontsize=13, transform=ax_data.transAxes,
                       family='monospace')
band_text = ax_data.text(0.1, 0.32, '', fontsize=13, transform=ax_data.transAxes,
                         family='monospace')

# Transmission angle bar
bar_bg = ax_data.barh(0.18, 1.0, height=0.06, color='lightgray',
                      transform=ax_data.transAxes, zorder=1)
bar_band = ax_data.axvspan(40/180, 140/180, ymin=0.15, ymax=0.24,
                           color='lightgreen', alpha=0.4, zorder=2)
ax_data.text(0.1, 0.10, '40°', fontsize=9, transform=ax_data.transAxes, color='gray')
ax_data.text(0.72, 0.10, '140°', fontsize=9, transform=ax_data.transAxes, color='gray')
ax_data.text(0.35, 0.10, 'Workable band', fontsize=9, transform=ax_data.transAxes,
             color='green', style='italic')
mu_bar, = ax_data.plot([], [], 'r|', markersize=30, markeredgewidth=3,
                       transform=ax_data.transAxes, zorder=3)

# Design info
info_lines = [
    "Haben's crossed-branch four-bar",
    f"L1={L1}, L2={L2}, L3={L3}, L4={L4} mm",
    f"Target: 40 mm jaw opening",
    f"Architecture A: 20T×20T spur pair, N=1",
]
for i, line in enumerate(info_lines):
    ax_data.text(0.5, 0.02 - i * 0.06 + 0.05, line, fontsize=9,
                 ha='center', transform=ax_data.transAxes, color='gray', style='italic')

tip_trail_x = []
tip_trail_y = []


def animate(frame):
    r = results[frame]
    if r is None:
        return link_line, tip_marker, tip_trail

    A, B = r['A'], r['B']
    tip = r['tip']

    # Update linkage
    xs = [O2[0], A[0], B[0], O4[0]]
    ys = [O2[1], A[1], B[1], O4[1]]
    link_line.set_data(xs, ys)

    tip_marker.set_data([tip[0]], [tip[1]])

    tip_trail_x.append(tip[0])
    tip_trail_y.append(tip[1])
    tip_trail.set_data(tip_trail_x, tip_trail_y)

    # Update data
    d = displacements[frame]
    mu = mus[frame]
    theta = thetas[frame]

    theta_text.set_text(f'Input angle:    {theta:+6.1f}°')
    disp_text.set_text(f'Displacement:   {d:6.2f} mm')
    jaw_text.set_text(f'Jaw opening:    {2*d:6.2f} mm (2×)')
    mu_text.set_text(f'Trans. angle:   {mu:6.1f}°')

    margin = mu - 40
    if margin > 15:
        band_text.set_text(f'Margin:         {margin:6.1f}° above floor  ✓')
        band_text.set_color('darkgreen')
    elif margin > 0:
        band_text.set_text(f'Margin:         {margin:6.1f}° above floor  ⚠')
        band_text.set_color('orange')
    else:
        band_text.set_text(f'Margin:         {margin:6.1f}° BELOW floor  ✗')
        band_text.set_color('red')

    mu_bar.set_data([mu / 180], [0.21])

    return link_line, tip_marker, tip_trail, theta_text, disp_text, jaw_text, mu_text, band_text, mu_bar


ani = animation.FuncAnimation(fig, animate, frames=N_FRAMES,
                              interval=50, blit=False, repeat=True)

plt.tight_layout()
plt.show()
