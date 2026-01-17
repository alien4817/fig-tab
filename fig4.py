import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np
import textwrap

# Figure 4: Service Cycle (High-Touch Patient Journey)
# Requirements addressed:
# 1) Circles use distinct colors and are labeled with numbers.
# 2) Title will not be covered (extra top margin + lower diagram center).
# 3) Text boxes placed outward with alternating radii to avoid overlap.

def wrap(s, width=30):
    return "\n".join(textwrap.wrap(s, width=width, break_long_words=False))

steps = [
    ("Local Access",
     "Patient visits an MOU hospital in Mongolia."),
    ("Tech Bridge",
     "Weekly 5G tele-consultation for diagnosis/plan."),
    ("Admin Support",
     "Visa assistance (≈80% market share)."),
    ("Cultural Arrival",
     '“Cultural Broker” (Mongolian spouse): airport pickup, accommodation, language support.'),
    ("Clinical Care",
     "District hospital agility + medical center support/transfer if needed."),
    ("Return & Continuity",
     "Follow-up by trained local nurses after returning home."),
]

# Distinct node colors (6 variations)
node_colors = ["#2E86AB", "#F18F01", "#A23B72", "#2E7D32", "#C1121F", "#6C3483"]

# ---- Canvas ----
fig, ax = plt.subplots(figsize=(12, 8.6))
ax.set_aspect("equal")
ax.axis("off")
ax.set_xlim(-7.8, 7.8)
ax.set_ylim(-6.4, 6.4)

# Title: placed high, with extra padding; diagram center moved downward
ax.text(
    0, 6.05, 'Figure 4: The "High-Touch" Patient Journey (Service Cycle)',
    ha="center", va="center", fontsize=16, weight="bold", zorder=50
)

# ---- Layout (shifted down to protect title area) ----
n = len(steps)
angles = np.linspace(np.pi/2, np.pi/2 - 2*np.pi, n, endpoint=False)  # start at top, clockwise

center = (0.0, -0.75)     # shift the whole cycle down so title is safe
node_ring_r = 3.05        # node radius ring
node_r = 0.58             # node circle radius
text_r_base = 4.55        # baseline text radius
text_r_list = [text_r_base + (0.75 if i % 2 == 0 else 0.20) for i in range(n)]  # alternate to reduce overlap

node_xy = []

# ---- Draw nodes + labels + outward text boxes ----
for i, (title, desc) in enumerate(steps):
    a = angles[i]
    nx = center[0] + node_ring_r * np.cos(a)
    ny = center[1] + node_ring_r * np.sin(a)
    node_xy.append((nx, ny))

    # Node circle with distinct color
    ax.add_patch(Circle((nx, ny), node_r, facecolor=node_colors[i], edgecolor="none", alpha=0.96, zorder=10))

    # Number label inside node
    ax.text(nx, ny, str(i + 1), ha="center", va="center",
            fontsize=14, weight="bold", color="white", zorder=12)

    # Text box position (farther out)
    tr = text_r_list[i]
    tx = center[0] + tr * np.cos(a)
    ty = center[1] + tr * np.sin(a)

    # Alignment by quadrant
    ha = "left" if np.cos(a) > 0.2 else ("right" if np.cos(a) < -0.2 else "center")
    va = "bottom" if np.sin(a) > 0.2 else ("top" if np.sin(a) < -0.2 else "center")

    box_text = f"{i+1}. {title}\n{wrap(desc, 32)}"

    ax.text(
        tx, ty, box_text,
        ha=ha, va=va, fontsize=10.5, weight="bold", color="#111111",
        bbox=dict(boxstyle="round,pad=0.42", facecolor="white", edgecolor="#333333",
                  linewidth=1.6, alpha=0.98),
        zorder=20
    )

    # Connector line to the text box (kept subtle)
    ax.plot([nx, tx], [ny, ty], linewidth=1.15, alpha=0.35, zorder=5)

# ---- Draw cycle arrows between nodes ----
for i in range(n):
    x1, y1 = node_xy[i]
    x2, y2 = node_xy[(i + 1) % n]

    # Create a small shrink so arrow doesn't touch node circles
    v1 = np.array([x1 - center[0], y1 - center[1]])
    v2 = np.array([x2 - center[0], y2 - center[1]])
    v1u = v1 / (np.linalg.norm(v1) + 1e-9)
    v2u = v2 / (np.linalg.norm(v2) + 1e-9)

    start = (x1 - v1u[0] * (node_r * 0.95), y1 - v1u[1] * (node_r * 0.95))
    end   = (x2 - v2u[0] * (node_r * 0.95), y2 - v2u[1] * (node_r * 0.95))

    ax.add_patch(FancyArrowPatch(
        start, end,
        arrowstyle="-|>", mutation_scale=18,
        linewidth=2.2, alpha=0.9,
        connectionstyle="arc3,rad=-0.25",  # clockwise curve
        zorder=8
    ))

# Center label
ax.text(
    center[0], center[1], "Service Cycle",
    ha="center", va="center", fontsize=12, weight="bold",
    bbox=dict(boxstyle="round,pad=0.35", facecolor="white",
              edgecolor="#2E86AB", linewidth=1.8, alpha=0.95),
    zorder=15
)

plt.tight_layout()
plt.savefig("Figure4_ServiceCycle_HighTouch_PatientJourney.png", dpi=300, bbox_inches="tight",
            facecolor="white", edgecolor="none")
plt.show()

print("Saved: Figure4_ServiceCycle_HighTouch_PatientJourney.png")
