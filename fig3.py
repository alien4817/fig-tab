import matplotlib.pyplot as plt
import numpy as np

# Data
years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
mou_hospitals = [2, 5, 8, 12, 12, 15, 16, 18, 20, 22]
trainees = [0, 4, 18, 13, 6, 0, 5, 11, 4, 17]

# Color coding for trainee types
# 2017-2019: Physician-focused (blue)
# 2020+: Shift to nursing/management (green/orange mix)
trainee_colors = ['#CCCCCC', '#4361EE', '#4361EE', '#4361EE', 
                  '#F9844A', '#CCCCCC', '#90BE6D', '#577590', '#CCCCCC', '#90BE6D']

# Create figure with dual axes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot bar chart for trainees (right axis)
ax2 = ax1.twinx()
bars = ax2.bar(years, trainees, color=trainee_colors, alpha=0.7, 
               width=0.6, edgecolor='white', linewidth=2, zorder=1)

# Plot line chart for MOU hospitals (left axis)
line = ax1.plot(years, mou_hospitals, color='#C1121F', marker='o', 
                linewidth=3, markersize=10, label='MOU Hospitals',
                zorder=3, markeredgecolor='white', markeredgewidth=2)

# Annotations for key points
ax1.annotate('Steady Growth', xy=(2022, 16), xytext=(2020, 18),
            arrowprops=dict(arrowstyle='->', color='#C1121F', lw=2),
            fontsize=10, color='#C1121F', weight='bold')

# Add annotation for shift to nursing management
ax2.text(2021.7, 7, 'Shift to Nursing\nManagement Training', 
        ha='center', va='bottom', fontsize=10, weight='bold',
        color='#577590',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF9E6', 
                 edgecolor='#577590', linewidth=2, alpha=0.9))

# Add annotation for pandemic impact
ax2.annotate('Pandemic\nOnline Training', xy=(2021, 0), xytext=(2021, -3),
            arrowprops=dict(arrowstyle='->', color='#888888', lw=1.5),
            fontsize=8, color='#888888', ha='center')

# Customize left y-axis (MOU Hospitals)
ax1.set_xlabel('Year', fontsize=12, weight='bold')
ax1.set_ylabel('Number of MOU Hospitals', fontsize=12, weight='bold', color='#C1121F')
ax1.tick_params(axis='y', labelcolor='#C1121F')
ax1.set_ylim(0, 25)
ax1.grid(True, axis='y', alpha=0.3, linestyle='--', zorder=0)

# Customize right y-axis (Trainees)
ax2.set_ylabel('Number of Trainees', fontsize=12, weight='bold', color='#4361EE')
ax2.tick_params(axis='y', labelcolor='#4361EE')
ax2.set_ylim(-5, 20)

# X-axis customization
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right')

# Add legend
legend_elements = [
    plt.Line2D([0], [0], color='#C1121F', linewidth=3, marker='o', 
               markersize=8, label='MOU Hospital Network'),
    plt.Rectangle((0, 0), 1, 1, fc='#4361EE', alpha=0.7, 
                  label='Physician Training (2017-2019)'),
    plt.Rectangle((0, 0), 1, 1, fc='#90BE6D', alpha=0.7, 
                  label='Nursing Management (2020+)'),
    plt.Rectangle((0, 0), 1, 1, fc='#F9844A', alpha=0.7, 
                  label='Mixed Training (2020)'),
]
ax1.legend(handles=legend_elements, loc='upper left', fontsize=10)

# Title
title_text = 'Figure 3: Capacity Building & Network Growth\nDual-Axis Chart (2016-2025)'
plt.title(title_text, fontsize=16, weight='bold', pad=20)

# Add note at bottom
fig.text(0.5, 0.02, 
         'Note: MOU network shows steady expansion while training focus shifted from physicians to nursing management post-2020',
         ha='center', fontsize=9, style='italic', color='#555555',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#F5F5F5', 
                  edgecolor='#CCCCCC', linewidth=1))

# Layout adjustment
plt.tight_layout()
plt.subplots_adjust(bottom=0.12)

# Save
plt.savefig('Figure3_Capacity_Building_Network_Growth.png', dpi=300, 
           bbox_inches='tight', facecolor='white', edgecolor='none')
plt.show()

print("✅ Figure 3 generated successfully!")
print("📁 Filename: 'Figure3_Capacity_Building_Network_Growth.png'")
print("📊 Dual-axis chart showing MOU growth and training trends")
print("🎯 Key insight: Shift to nursing management training highlighted")