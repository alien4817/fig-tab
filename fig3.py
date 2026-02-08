import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# =========================
# Figure 3 data (hard-coded)
# =========================
years = np.arange(2016, 2026)

# Left axis (line): cumulative number of MOU partner hospitals
mou_hospitals_cum = np.array([2, 5, 8, 12, 12, 15, 16, 18, 20, 22])

# Right axis (stacked bars): annual trainees by role
# 2016補0；2017–2025來自你的表
physicians = np.array([0, 4, 18, 13, 6, 0, 4, 9, 4, 5])
nurses_others = np.array([0, 0, 0, 0, 0, 0, 1, 2, 0, 12])  # 2025: 11 nurses + 1 technician
total_trainees = physicians + nurses_others

# =========================
# Style settings (journal-friendly)
# =========================
LINE_COLOR = "#C1121F"        # MOU line
PHYS_COLOR = "#4361EE"        # Physicians
NONPHYS_COLOR = "#F9844A"     # Nurses/Others
EDGE_COLOR = "white"

# =========================
# Plot: dual-axis + stacked bars
# =========================
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

bar_w = 0.65

# Stacked bars (right axis)
bars_phys = ax2.bar(
    years, physicians,
    width=bar_w, color=PHYS_COLOR, alpha=0.85,
    edgecolor=EDGE_COLOR, linewidth=1.8, zorder=2
)
bars_non = ax2.bar(
    years, nurses_others, bottom=physicians,
    width=bar_w, color=NONPHYS_COLOR, alpha=0.85,
    edgecolor=EDGE_COLOR, linewidth=1.8, zorder=2
)

# Line (left axis)
ax1.plot(
    years, mou_hospitals_cum,
    color=LINE_COLOR, marker="o", linewidth=3, markersize=9,
    markeredgecolor="white", markeredgewidth=2,
    zorder=4
)

# =========================
# Annotations
# =========================
# 2025 highlight
x2025 = 2025
idx_2025 = np.where(years == 2025)[0][0]
y2025_total = total_trainees[idx_2025]

ax2.text(
    x2025, y2025_total + 0.6,
    "Shift to Nursing\nEmpowerment",
    ha="center", va="bottom", fontsize=10, weight="bold",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#FFF9E6",
              edgecolor="#333333", linewidth=1.6, alpha=0.95),
    zorder=6
)

ax2.text(
    x2025, y2025_total - 0.2,
    f"{int(physicians[idx_2025])} physicians\n{int(nurses_others[idx_2025])} non-phys",
    ha="center", va="top", fontsize=9,
    bbox=dict(boxstyle="round,pad=0.35", facecolor="white",
              edgecolor="#999999", linewidth=1.2, alpha=0.9),
    zorder=6
)

# Optional: pandemic note (2021 total = 0)
idx_2021 = np.where(years == 2021)[0][0]
if total_trainees[idx_2021] == 0:
    ax2.annotate(
        "Pandemic\n(online / pause)",
        xy=(2021, 0),
        xytext=(2021, max(y2025_total * 0.18, 2)),
        ha="center", fontsize=9,
        arrowprops=dict(arrowstyle="->", lw=1.5),
        zorder=6
    )

# Optional: steady growth label on the line
ax1.annotate(
    "Steady Growth",
    xy=(2022, mou_hospitals_cum[np.where(years == 2022)[0][0]]),
    xytext=(2020.2, mou_hospitals_cum[np.where(years == 2022)[0][0]] + 3),
    arrowprops=dict(arrowstyle="->", color=LINE_COLOR, lw=2),
    fontsize=10, color=LINE_COLOR, weight="bold",
    zorder=6
)

# =========================
# Axes formatting
# =========================
ax1.set_xlabel("Year", fontsize=12, weight="bold")
ax1.set_ylabel("Number of MOU Hospitals (cumulative)", fontsize=12, weight="bold", color=LINE_COLOR)
ax2.set_ylabel("Number of Trainees (stacked)", fontsize=12, weight="bold")

ax1.tick_params(axis="y", labelcolor=LINE_COLOR)

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha="right")

ax1.set_ylim(0, max(mou_hospitals_cum.max() + 3, 10))
ax2.set_ylim(0, total_trainees.max() + 5)

ax1.grid(True, axis="y", linestyle="--", alpha=0.25, zorder=0)

# =========================
# Legend (FIXED: true mapping to line + bar colors)
# =========================
legend_handles = [
    Line2D(
        [0], [0],
        color=LINE_COLOR, linewidth=3,
        marker="o", markersize=8,
        markeredgecolor="white", markeredgewidth=2,
        label="MOU Hospital Network"
    ),
    Patch(
        facecolor=PHYS_COLOR, edgecolor=EDGE_COLOR, linewidth=1.5,
        label="Physicians"
    ),
    Patch(
        facecolor=NONPHYS_COLOR, edgecolor=EDGE_COLOR, linewidth=1.5,
        label="Nurses / Others"
    ),
]

ax1.legend(
    handles=legend_handles,
    loc="upper left",
    frameon=True,
    fontsize=11
)

# =========================
# Title + footnote
# =========================
plt.title(
    "Figure 3: Capacity Building & Network Growth\n"
    "Dual-Axis Chart (2016-2025)",
    fontsize=15, weight="bold", pad=18
)

fig.text(
    0.5, 0.02,
    "Note: The MOU network expanded steadily, while training shifted toward nursing capacity building in 2025.",
    ha="center", fontsize=9, style="italic"
)

plt.tight_layout()
plt.subplots_adjust(bottom=0.12)

# =========================
# Save
# =========================
out_png = "Figure3_Capacity_Building_Network_Growth.png"
plt.savefig(out_png, dpi=300, bbox_inches="tight", facecolor="white")
plt.show()

print("✅ Figure 3 generated successfully!")
print(f"📁 Filename: {out_png}")
print("📊 MOU hospitals (cumulative):", mou_hospitals_cum.tolist())
print("📊 Trainees total:", total_trainees.tolist())