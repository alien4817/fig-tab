import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Create figure
fig, ax = plt.subplots(figsize=(20, 10))
ax.set_xlim(0, 11)
ax.set_ylim(0, 11)  # Increased y limit
ax.axis('off')

# Draw main timeline (moved down)
timeline_y = 5
ax.plot([1, 10], [timeline_y, timeline_y], 'k-', linewidth=3, zorder=1)

# Timeline milestones (x positions)
milestones = {
    '2016': 1.5,
    '2019': 3.5,
    '2020-2022': 5.5,
    '2025': 7.5,
    '2026': 9.5
}

# Colors for each phase
colors = {
    '2016': '#90BE6D',
    '2019': '#F9C74F',
    '2020-2022': '#F94144',
    '2025': '#577590',
    '2026': '#4361EE'
}

# Milestone data
milestone_data = {
    '2016': {
        'title': '2016\nInitiation',
        'items': ['Platform Launch', 'First MOUs Signed'],
        'y_offset': 0,
        'highlight': False
    },
    '2019': {
        'title': '2019\nPeak Engagement',
        'items': ['Large-scale Medical Missions', 'Physician Training Peak'],
        'y_offset': 0,
        'highlight': False
    },
    '2020-2022': {
        'title': '2020-2022\nResilience Phase',
        'items': [
            'Crisis Response: Zero Service Interruption',
            'Tech: 5G Smart Glasses Deployed',
            'Nursing: Nursing Directors On-site',
            'Admin: 100% Medical Visa Success'
        ],
        'y_offset': 1.5,
        'highlight': True
    },
    '2025': {
        'title': '2025\nScalability',
        'items': [
            'Vietnam Expansion: MOU with Sakura',
            'Complex Cases: Neurosurgery/IVF Referrals'
        ],
        'y_offset': 0,
        'highlight': False
    },
    '2026': {
        'title': '2026\nInstitutionalization',
        'items': [
            'Launch: "Weekly Tele-consultation"',
            'From "Ad-hoc" to "Routine"'
        ],
        'y_offset': 2,
        'highlight': True
    }
}

# Draw milestones
for year, x_pos in milestones.items():
    data = milestone_data[year]
    color = colors[year]
    y_base = timeline_y + data['y_offset']
    
    # Draw connector line from timeline to box
    ax.plot([x_pos, x_pos], [timeline_y, y_base + 0.5], 
            color=color, linewidth=2.5, zorder=2)
    
    # Draw circle marker on timeline
    circle = plt.Circle((x_pos, timeline_y), 0.15, 
                       color=color, ec='white', linewidth=2, zorder=3)
    ax.add_patch(circle)
    
    # Create box for milestone content
    box_width = 1.6
    box_height = 0.8 + len(data['items']) * 0.25
    
    if data['highlight']:
        # Highlighted box with thicker border
        box = FancyBboxPatch((x_pos - box_width/2, y_base + 0.5), 
                            box_width, box_height,
                            boxstyle="round,pad=0.1",
                            facecolor=color, edgecolor='#000000',
                            linewidth=4, alpha=0.9, zorder=4)
        # Add "HIGHLIGHT" label
        ax.text(x_pos, y_base + box_height + 0.8, '★ HIGHLIGHT ★',
               ha='center', va='center', fontsize=9, weight='bold',
               color=color,
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                        edgecolor=color, linewidth=2))
    else:
        box = FancyBboxPatch((x_pos - box_width/2, y_base + 0.5), 
                            box_width, box_height,
                            boxstyle="round,pad=0.1",
                            facecolor=color, edgecolor='white',
                            linewidth=2, alpha=0.85, zorder=4)
    
    ax.add_patch(box)
    
    # Add title
    ax.text(x_pos, y_base + box_height + 0.2, data['title'],
           ha='center', va='top', fontsize=11, weight='bold',
           color='white', zorder=5)
    
    # Add items
    y_text = y_base + box_height - 0.3
    for item in data['items']:
        ax.text(x_pos, y_text, f'• {item}',
               ha='center', va='top', fontsize=7.5,
               color='white', zorder=5)
        y_text -= 0.25

# Add title (moved up with more spacing)
title_box = FancyBboxPatch((0.5, 10), 10, 0.7,
                          boxstyle="round,pad=0.15",
                          facecolor='#2E86AB', edgecolor='#1565C0',
                          linewidth=3, alpha=0.9, zorder=10)
ax.add_patch(title_box)
ax.text(5.5, 10.35, 'Figure 2: The Timeline of Resilience & Expansion (2016-2026)',
       ha='center', va='center', fontsize=16, weight='bold',
       color='white', zorder=11)

# Add timeline arrows at both ends
ax.annotate('', xy=(10.3, timeline_y), xytext=(10, timeline_y),
           arrowprops=dict(arrowstyle='->', lw=3, color='black'))

# Add legend for phases (moved down)
legend_y = 0.8
ax.text(5.5, legend_y, 'Evolution: Initiation → Peak → Resilience → Scalability → Institutionalization',
       ha='center', va='center', fontsize=10, style='italic',
       color='#555555',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#F0F0F0',
                edgecolor='#CCCCCC', linewidth=2))

# Save
plt.tight_layout()
plt.savefig('Figure2_Timeline_Resilience_Expansion.png', dpi=300, 
           bbox_inches='tight', facecolor='white', edgecolor='none')
plt.show()

print("✅ Figure 2 generated successfully!")
print("📁 Filename: 'Figure2_Timeline_Resilience_Expansion.png'")
print("✨ Title spacing fixed - no more overlap with timeline")