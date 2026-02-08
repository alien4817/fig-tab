import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np
import textwrap

# Figure 4: The "High-Touch" Patient Journey (Service Cycle)
# 修正重點（對齊 @+6 要求）：
# 1) 圖型：循環流程圖（Service Cycle）
# 2) 6 個必備觸點皆保留，文字更貼近論文敘事（Local→Tech→Admin(80%)→Cultural(Cultural Brokerage)→Clinical(vertical referral)→Return）
# 3) 明確把兩個「關鍵價值點」做成醒目徽章（badges）：
#    - "≈80% Market Share" 放在 Admin Support
#    - "Cultural Brokerage" 放在 Cultural Arrival
# 4) Clinical Care 明確寫出「必要時垂直轉介醫學中心」（連回 Figure 1 的 vertical integration）

def wrap(s, width=32):
    return "\n".join(textwrap.wrap(s, width=width, break_long_words=False))

# ---- 6 touchpoints (wording aligned with @+6) ----
steps = [
    ("Local Access",
     "Patient enters the system via a Mongolia MOU partner hospital (local entry point)."),
    ("Tech Bridge",
     "Weekly 5G tele-consultation enables triage, diagnosis, and care planning."),
    ("Admin Support",
     "Visa & logistics support that reduces friction and drives conversion (≈80% visa market share)."),
    ("Cultural Arrival",
     "Diaspora Navigator (Mongolian spouse) provides airport pickup, translation, and settlement support."),
    ("Clinical Care",
     "Care at Yuan Rung Hospital; vertical referral to tertiary medical centers when needed."),
    ("Return & Continuity",
     "Post-return follow-up by locally trained nurses to close the loop and sustain outcomes."),
]

# Distinct node colors
node_colors = ["#2E86AB", "#F18F01", "#A23B72", "#2E7D32", "#C1121F", "#6C3483"]

# ---- Badges: enforce the two key value points (must-have per @+6) ----
# badge_text, step_index, (dx,dy) offset in data coords, color
badges = [
    ("≈80% Market Share", 2, (0.0, 1.05), "#A23B72"),   # Admin Support
    ("Cultural Brokerage", 3, (0.0, 1.05), "#2E7D32"),  # Cultural Arrival
]

# ---- Canvas ----
fig, ax = plt.subplots(figsize=(12, 8.8))
ax.set_aspect("equal")
ax.axis("off")
ax.set_xlim(-7.9, 7.9)
ax.set_ylim(-6.6, 6.6)

# Title (keep safe margin)
ax.text(
    0, 6.1, 'Figure 4: The "High-Touch" Patient Journey (Service Cycle)',
    ha="center", va="center", fontsize=16, weight="bold", zorder=50
)

# ---- Layout: shift down to protect title area ----
n = len(steps)
angles = np.linspace(np.pi/2, np.pi/2 - 2*np.pi, n, endpoint=False)  # start at top, clockwise

center = (0.0, -0.80)   # shift the cycle down
node_ring_r = 3.05
node_r = 0.58

# Text radius (alternate to reduce overlap)
text_r_base = 4.65
text_r_list = [text_r_base + (0.85 if i % 2 == 0 else 0.25) for i in range(n)]

node_xy = []

# ---- Draw nodes + numbered labels + outward text boxes ----
for i, (title, desc) in enumerate(steps):
    a = angles[i]
    nx = center[0] + node_ring_r * np.cos(a)
    ny = center[1] + node_ring_r * np.sin(a)
    node_xy.append((nx, ny))

    # Node circle
    ax.add_patch(
        Circle((nx, ny), node_r,
               facecolor=node_colors[i], edgecolor="none", alpha=0.96, zorder=10)
    )

    # Number inside node
    ax.text(
        nx, ny, str(i + 1),
        ha="center", va="center",
        fontsize=14, weight="bold", color="white", zorder=12
    )

    # Text box outward position
    tr = text_r_list[i]
    tx = center[0] + tr * np.cos(a)
    ty = center[1] + tr * np.sin(a)

    # Alignment based on quadrant
    ha = "left" if np.cos(a) > 0.2 else ("right" if np.cos(a) < -0.2 else "center")
    va = "bottom" if np.sin(a) > 0.2 else ("top" if np.sin(a) < -0.2 else "center")

    box_text = f"{i+1}. {title}\n{wrap(desc, 34)}"

    ax.text(
        tx, ty, box_text,
        ha=ha, va=va, fontsize=10.5, weight="bold", color="#111111",
        bbox=dict(
            boxstyle="round,pad=0.42",
            facecolor="white", edgecolor="#333333",
            linewidth=1.6, alpha=0.98
        ),
        zorder=20
    )

    # Connector line to text box
    ax.plot([nx, tx], [ny, ty], linewidth=1.15, alpha=0.30, zorder=5)

# ---- Draw cycle arrows between nodes ----
for i in range(n):
    x1, y1 = node_xy[i]
    x2, y2 = node_xy[(i + 1) % n]

    # Shrink arrow ends so they don't touch node circles
    v1 = np.array([x1 - center[0], y1 - center[1]])
    v2 = np.array([x2 - center[0], y2 - center[1]])
    v1u = v1 / (np.linalg.norm(v1) + 1e-9)
    v2u = v2 / (np.linalg.norm(v2) + 1e-9)

    start = (x1 - v1u[0] * (node_r * 0.95), y1 - v1u[1] * (node_r * 0.95))
    end   = (x2 - v2u[0] * (node_r * 0.95), y2 - v2u[1] * (node_r * 0.95))

    ax.add_patch(
        FancyArrowPatch(
            start, end,
            arrowstyle="-|>", mutation_scale=18,
            linewidth=2.2, alpha=0.9,
            connectionstyle="arc3,rad=-0.25",  # clockwise curve
            zorder=8
        )
    )

# ---- Center label ----
ax.text(
    center[0], center[1],
    "Service Cycle",
    ha="center", va="center", fontsize=12, weight="bold",
    bbox=dict(
        boxstyle="round,pad=0.35",
        facecolor="white",
        edgecolor="#2E86AB",
        linewidth=1.8, alpha=0.95
    ),
    zorder=15
)

# ---- Add MUST-HAVE badges (≈80% Market Share / Cultural Brokerage) ----
for badge_text, idx, (dx, dy), c in badges:
    bx, by = node_xy[idx]
    ax.text(
        bx + dx, by + dy,
        badge_text,
        ha="center", va="center",
        fontsize=10, weight="bold", color=c,
        bbox=dict(
            boxstyle="round,pad=0.35",
            facecolor="#FFFFFF",
            edgecolor=c,
            linewidth=2.0,
            alpha=0.98
        ),
        zorder=30
    )

# Optional: subtle subtitle/footnote (safe for journals)
fig.text(
    0.5, 0.02,
    'Key drivers highlighted: "≈80% Market Share" (Admin Support) and "Cultural Brokerage" (Cultural Arrival).',
    ha="center", fontsize=9, style="italic", color="#444444"
)

plt.tight_layout()
plt.savefig(
    "Figure4_ServiceCycle_HighTouch_PatientJourney.png",
    dpi=300, bbox_inches="tight", facecolor="white", edgecolor="none"
)
plt.show()

print("Saved: Figure4_ServiceCycle_HighTouch_PatientJourney.png")