import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np

# Create figure
fig, ax = plt.subplots(figsize=(18, 14))
ax.set_xlim(-11, 11)
ax.set_ylim(-9, 9)
ax.axis('off')

# ===== Concentric Circle Structure =====
# Outermost layer: Global Network
outer_circle = Circle((0, 0), 7.5, color="#88D9F4", alpha=0.3, 
                      edgecolor='#2E86AB', linewidth=2, linestyle='--', zorder=1)
ax.add_patch(outer_circle)
ax.text(0, 7.8, 'Global Network Layer', ha='center', va='center', 
        fontsize=11, style='italic', color='#2E86AB', weight='bold')

# Second layer: Strategic Alliance
middle_circle = Circle((0, 0), 5.5, color="#F7E097", alpha=0.4, 
                       edgecolor='#F18F01', linewidth=2, linestyle='--', zorder=2)
ax.add_patch(middle_circle)
ax.text(0, 5.8, 'Strategic Alliance Layer', ha='center', va='center', 
        fontsize=11, style='italic', color='#F18F01', weight='bold')

# Third layer: Integration Platform
inner_circle = Circle((0, 0), 3.5, color="#D092F4", alpha=0.4, 
                      edgecolor='#A23B72', linewidth=2, linestyle='--', zorder=3)
ax.add_patch(inner_circle)
ax.text(0, 3.8, 'Integration Platform Layer', ha='center', va='center', 
        fontsize=11, style='italic', color='#A23B72', weight='bold')

# Fourth layer: Core Hub
core_circle = Circle((0, 0), 2, color='#E3F2FD', alpha=0.6, 
                     edgecolor='#2E86AB', linewidth=2.5, zorder=4)
ax.add_patch(core_circle)

# ===== Center Hub =====
center_circle = Circle((0, 0), 1.4, color="#0F77A4", alpha=0.95, zorder=5)
ax.add_patch(center_circle)

# Center text
ax.text(0, 0.5, 'Yuan Rung Hospital', ha='center', va='center', 
        fontsize=16, weight='bold', color='orange', zorder=6)
ax.text(0, 0, '(District Hospital)', ha='center', va='center', 
        fontsize=11, color='white', zorder=6)
ax.text(0, -0.5, 'Resource Integrator', ha='center', va='center', 
        fontsize=11, weight='bold', color='#FFF9E6', zorder=6)

# Core functions around the hub
core_functions = [
    ('Patient\nCoordination', -1.2, 2.5, 0),
    ('Quality\nControl', 1.2, 2.5, 0),
    ('Cultural\nBrokerage', -2.5, -0.3, 270),
    ('Admin\nSupport', 2.5, -0.3, 90)
]

for text, x, y, rotation in core_functions:
    ax.text(x, y, text, ha='center', va='center', 
            fontsize=8, color='#A23B72', weight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                     edgecolor='#A23B72', linewidth=1.5, alpha=0.9),
            rotation=rotation, zorder=4)

# ===== Left: Vertical Integration =====
# Title
ax.text(-7.5, 7, 'Vertical Integration', ha='center', va='center', 
        fontsize=15, weight='bold', color='#A23B72')
ax.text(-7.5, 6.4, 'The Taiwan Team', ha='center', va='center', 
        fontsize=12, style='italic', color='#A23B72')

# Medical Centers label
ax.text(-8.5, 4.5, '[ Medical Centers ]', ha='center', va='center', 
        fontsize=10, weight='bold', color='#A23B72',
        bbox=dict(boxstyle='round', facecolor='#FFF9E6', alpha=0.8))

# Medical Centers
medical_centers = [
    ('Tri-Service General\nHospital', -8.5, 3.2),
    ('Taichung Veterans\nGeneral Hospital', -8.5, 1.7),
    ('Chang Gung Memorial\nHospital', -8.5, 0.2)
]

for name, x, y in medical_centers:
    box = FancyBboxPatch((x-1.1, y-0.5), 2.2, 1, 
                          boxstyle="round,pad=0.12", 
                          facecolor='#F18F01', edgecolor='#A23B72', 
                          linewidth=2.5, alpha=0.9, zorder=3)
    ax.add_patch(box)
    ax.text(x, y, name, ha='center', va='center', fontsize=8.5, weight='bold')
    
    # Connection to center
    arrow = FancyArrowPatch((x+1.1, y), (-1.4, 0),
                           arrowstyle='->', mutation_scale=25, 
                           linewidth=3, color='#A23B72', alpha=0.7, zorder=2,
                           connectionstyle="arc3,rad=0.1")
    ax.add_patch(arrow)

# Connection label
ax.text(-4.5,-0.3, 'Green Channel\nTertiary Support', 
        ha='center', va='center',
        fontsize=14, 
        weight='bold', 
        color='#A23B72',
        rotation=270,  # 文字直的
        bbox=dict(
            boxstyle='round,pad=1.0',  # ← 把 pad 加大 (原本0.4)
            facecolor='#E8F5E9',
            edgecolor='#4CAF50',
            linewidth=3,   # 邊框粗一點
            alpha=1        # 完全不透明
        ),
        zorder=100)       # 保證蓋過所有線

# Specialty Alliances label
ax.text(-8.5, -1, '[ Specialty Alliances ]', ha='center', va='center', 
        fontsize=10, weight='bold', color='#A23B72',
        bbox=dict(boxstyle='round', facecolor='#FFF9E6', alpha=0.8))

# Specialty Alliances
specialty_alliances = [
    ('Lee Women\'s Hospital\n(IVF Center)', -8.5, -2),
    ('Bai\'s Eye Clinic', -8.5, -3.5)
]

for name, x, y in specialty_alliances:
    box = FancyBboxPatch((x-1.1, y-0.5), 2.2, 1, 
                          boxstyle="round,pad=0.12", 
                          facecolor='#90BE6D', edgecolor='#A23B72', 
                          linewidth=2.5, alpha=0.9, zorder=3)
    ax.add_patch(box)
    ax.text(x, y, name, ha='center', va='center', fontsize=8.5, weight='bold')
    
    # Connection to center
    arrow = FancyArrowPatch((x+1.1, y), (-1.4, -0.2),
                           arrowstyle='->', mutation_scale=25, 
                           linewidth=3, color='#A23B72', alpha=0.7, zorder=2,
                           connectionstyle="arc3,rad=-0.1")
    ax.add_patch(arrow)

# ===== Right: Horizontal Expansion =====
# Title
ax.text(7.5, 7, 'Horizontal Expansion', ha='center', va='center', 
        fontsize=15, weight='bold', color='#C1121F')
ax.text(7.5, 6.4, 'Mongolia Network', ha='center', va='center', 
        fontsize=12, style='italic', color='#C1121F')

# Connection label
ax.text(4.5, -0.3, 'Capacity Building\n& Patient Referral', 
        ha='center', va='center',
        fontsize=14, weight='bold', color='#C1121F', 
        rotation=90,  # 文字直的
        bbox=dict(boxstyle='round,pad=1', facecolor='#FFEBEE', 
                 edgecolor='#C1121F', linewidth=2, alpha=0.95), zorder=4)

# Tertiary Level
ax.text(8.5, 4.5, '[ Tertiary Level ]', ha='center', va='center', 
        fontsize=10, weight='bold', color='#C1121F',
        bbox=dict(boxstyle='round', facecolor='#FFEBEE', alpha=0.8))

tertiary_level = [
    ('First Central\nHospital', 8.5, 3.5),
    ('Fourth Hospital', 8.5, 2.5)
]

for name, x, y in tertiary_level:
    box = FancyBboxPatch((x-0.9, y-0.35), 1.8, 0.7, 
                          boxstyle="round,pad=0.1", 
                          facecolor='#E63946', edgecolor='#C1121F', 
                          linewidth=2.5, alpha=0.9, zorder=3)
    ax.add_patch(box)
    ax.text(x, y, name, ha='center', va='center', fontsize=8, weight='bold')
    
    # Connection to center
    arrow = FancyArrowPatch((x-0.9, y), (1.4, 0),
                           arrowstyle='<-', mutation_scale=25, 
                           linewidth=3, color='#C1121F', alpha=0.7, zorder=2,
                           connectionstyle="arc3,rad=0.1")
    ax.add_patch(arrow)

# District Level
ax.text(8.5, 1.3, '[ District Level ]', ha='center', va='center', 
        fontsize=10, weight='bold', color='#C1121F',
        bbox=dict(boxstyle='round', facecolor='#FFEBEE', alpha=0.8))

district_level = [
    ('Bayanzurkh\nDistrict Center', 8.5, 0.5),
    ('Community Health\nCenters (x8)', 8.5, -0.5)
]

for name, x, y in district_level:
    box = FancyBboxPatch((x-0.9, y-0.35), 1.8, 0.7, 
                          boxstyle="round,pad=0.1", 
                          facecolor='#FCA311', edgecolor='#C1121F', 
                          linewidth=2.5, alpha=0.9, zorder=3)
    ax.add_patch(box)
    ax.text(x, y, name, ha='center', va='center', fontsize=8, weight='bold')
    
    # Connection to center
    arrow = FancyArrowPatch((x-0.9, y), (1.4, 0),
                           arrowstyle='<-', mutation_scale=25, 
                           linewidth=3, color='#C1121F', alpha=0.7, zorder=2)
    ax.add_patch(arrow)

# Specialty Level
ax.text(8.5, -1.8, '[ Specialty Level ]', ha='center', va='center', 
        fontsize=10, weight='bold', color='#C1121F',
        bbox=dict(boxstyle='round', facecolor='#FFEBEE', alpha=0.8))

specialty_level = [
    ('National\nDermatology Center', 8.5, -2.6),
    ('Specialty Centers\n(x12)', 8.5, -3.6)
]

for name, x, y in specialty_level:
    box = FancyBboxPatch((x-0.9, y-0.35), 1.8, 0.7, 
                          boxstyle="round,pad=0.1", 
                          facecolor='#06A77D', edgecolor='#C1121F', 
                          linewidth=2.5, alpha=0.9, zorder=3)
    ax.add_patch(box)
    ax.text(x, y, name, ha='center', va='center', fontsize=8, weight='bold')
    
    # Connection to center
    arrow = FancyArrowPatch((x-0.9, y), (1.4, -0.2),
                           arrowstyle='<-', mutation_scale=25, 
                           linewidth=3, color='#C1121F', alpha=0.7, zorder=2,
                           connectionstyle="arc3,rad=-0.1")
    ax.add_patch(arrow)

# 22 MOU Partners
ax.text(7.5, -4.8, '22 MOU Partners', ha='center', va='center',
        fontsize=12, weight='bold', color='white',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#C1121F', 
                 edgecolor='#780000', linewidth=3, alpha=0.95))

# ===== Foundation =====
# Foundation background
foundation_bg = Rectangle((-5, -7.5), 10, 2.5, 
                         facecolor='#577590', alpha=0.2, 
                         edgecolor='#577590', linewidth=3, zorder=1)
ax.add_patch(foundation_bg)

ax.text(0, -5.3, '== FOUNDATION ==', ha='center', va='center', 
        fontsize=14, weight='bold', color='#577590')

# Left pillar: Nursing Empowerment
pillar1 = FancyBboxPatch((-4.2, -7.3), 3.8, 1.4, 
                         boxstyle="round,pad=0.15", 
                         facecolor='#4A5759', edgecolor='#577590', 
                         linewidth=3, alpha=0.95, zorder=2)
ax.add_patch(pillar1)
ax.text(-2.3, -6.5, 'Nursing Empowerment', ha='center', va='center', 
        fontsize=11, weight='bold', color='white')
ax.text(-2.3, -7.1, '(Triage, SOPs, IPSG)', ha='center', va='center', 
        fontsize=9, style='italic', color='#B0BEC5')

# Right pillar: 5G Resilience
pillar2 = FancyBboxPatch((0.4, -7.3), 3.8, 1.4, 
                         boxstyle="round,pad=0.15", 
                         facecolor='#4A5759', edgecolor='#577590', 
                         linewidth=3, alpha=0.95, zorder=2)
ax.add_patch(pillar2)
ax.text(2.3, -6.5, '5G Resilience', ha='center', va='center', 
        fontsize=11, weight='bold', color='white')
ax.text(2.3, -7.1, '(Telementoring, Weekly Tele-clinic)', ha='center', va='center', 
        fontsize=9, style='italic', color='#B0BEC5')

# ===== Title =====
title_box = FancyBboxPatch((-6.5, 8.2), 13, 0.8, 
                           boxstyle="round,pad=0.2", 
                           facecolor='#2E86AB', edgecolor='#1565C0', 
                           linewidth=3, alpha=0.9, zorder=10)
ax.add_patch(title_box)
ax.text(0, 8.6, 'Figure 1: The "Yuan Rung Ecosystem" Architecture', 
        ha='center', va='center', fontsize=17, weight='bold', color='white', zorder=11)

# Save
plt.tight_layout()
plt.savefig('Figure1_Yuan_Rung_Ecosystem_Final.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.show()

print("✅ Figure generated successfully!")
print("📁 Filename: 'Figure1_Yuan_Rung_Ecosystem_Final.png'")