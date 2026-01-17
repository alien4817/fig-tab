import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Wedge
import numpy as np

# Create figure
fig, ax = plt.subplots(figsize=(16, 16))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

# Center circle
center_circle = Circle((0, 0), 1, color='#2E86AB', alpha=0.95, zorder=5)
ax.add_patch(center_circle)
ax.text(0, 0.2, 'Patient', ha='center', va='center', 
        fontsize=13, weight='bold', color='white', zorder=6)
ax.text(0, -0.25, 'Journey', ha='center', va='center', 
        fontsize=11, weight='bold', color='white', zorder=6)

# Define 6 stages with better spacing
stages = [
    {
        'num': '1',
        'title': 'Local Access',
        'location': 'In Mongolia',
        'desc': ['Patient visits', 'MOU Hospital'],
        'angle': 90,
        'color': '#90BE6D',
        'box_offset': 0  # No offset
    },
    {
        'num': '2',
        'title': 'Tech Bridge',
        'location': '5G Platform',
        'desc': ['Weekly 5G', 'Tele-consultation'],
        'angle': 30,
        'color': '#4361EE',
        'box_offset': 0
    },
    {
        'num': '3',
        'title': 'Admin Support',
        'location': '80% Market Share',
        'desc': ['Visa Assistance', 'Travel Setup'],
        'angle': -30,
        'color': '#F9844A',
        'box_offset': 0
    },
    {
        'num': '4',
        'title': 'Cultural Arrival',
        'location': 'Cultural Broker',
        'desc': ['Airport Pickup', 'Accommodation', 'Language Support'],
        'angle': -90,
        'color': '#F9C74F',
        'box_offset': 0.3  # Slightly larger box
    },
    {
        'num': '5',
        'title': 'Clinical Care',
        'location': 'In Taiwan',
        'desc': ['District Hospital', '+ Medical Center', 'Support'],
        'angle': -150,
        'color': '#E63946',
        'box_offset': 0.2
    },
    {
        'num': '6',
        'title': 'Return & Continuity',
        'location': 'Back to Mongolia',
        'desc': ['Follow-up by', 'Local Nurses'],
        'angle': 150,
        'color': '#577590',
        'box_offset': 0
    }
]

# Draw stages - well-spaced layout
radius = 6.5
for stage in stages:
    angle_rad = np.radians(stage['angle'])
    x = radius * np.cos(angle_rad)
    y = radius * np.sin(angle_rad)
    
    # Box dimensions based on content
    box_width = 2.4
    box_height = 2.0 + stage['box_offset']
    
    # Draw stage box
    box = FancyBboxPatch((x - box_width/2, y - box_height/2), 
                         box_width, box_height,
                         boxstyle="round,pad=0.1",
                         facecolor=stage['color'], 
                         edgecolor='white',
                         linewidth=2.5, alpha=0.9, zorder=3)
    ax.add_patch(box)
    
    # Step number badge at top
    badge_y = y + box_height/2 - 0.25
    badge = Circle((x, badge_y), 0.22, color='white', alpha=1, zorder=4)
    ax.add_patch(badge)
    ax.text(x, badge_y, stage['num'],
           ha='center', va='center', fontsize=11, weight='bold',
           color=stage['color'], zorder=5)
    
    # Title
    title_y = y + box_height/2 - 0.65
    ax.text(x, title_y, stage['title'],
           ha='center', va='center', fontsize=10, weight='bold',
           color='white', zorder=4)
    
    # Location/subtitle
    location_y = title_y - 0.28
    ax.text(x, location_y, stage['location'],
           ha='center', va='center', fontsize=7.5, style='italic',
           color='white', alpha=0.95, zorder=4)
    
    # Description lines
    desc_start_y = location_y - 0.35
    for i, line in enumerate(stage['desc']):
        ax.text(x, desc_start_y - (i * 0.22), line,
               ha='center', va='center', fontsize=7.5,
               color='white', zorder=4)
    
    # Connecting line to center
    inner_r = 1.3
    outer_r = radius - 1.4
    
    x_in = inner_r * np.cos(angle_rad)
    y_in = inner_r * np.sin(angle_rad)
    x_out = outer_r * np.cos(angle_rad)
    y_out = outer_r * np.sin(angle_rad)
    
    connector = FancyArrowPatch((x_in, y_in), (x_out, y_out),
                               arrowstyle='<->', mutation_scale=15,
                               linewidth=1.8, color=stage['color'], 
                               alpha=0.4, zorder=2)
    ax.add_patch(connector)

# Draw circular flow arrows
flow_radius = 8.2
for i in range(len(stages)):
    next_i = (i + 1) % len(stages)
    
    angle1 = stages[i]['angle']
    angle2 = stages[next_i]['angle']
    
    # Handle wraparound
    if i == len(stages) - 1:
        angle2 += 360
    
    # Calculate arc points
    arc_span = 15  # degrees from each box
    start_angle = angle1 - arc_span
    end_angle = angle2 + arc_span
    
    x1 = flow_radius * np.cos(np.radians(start_angle))
    y1 = flow_radius * np.sin(np.radians(start_angle))
    x2 = flow_radius * np.cos(np.radians(end_angle))
    y2 = flow_radius * np.sin(np.radians(end_angle))
    
    # Curved arrow
    flow_arrow = FancyArrowPatch((x1, y1), (x2, y2),
                                arrowstyle='->', mutation_scale=20,
                                linewidth=2.5, color='#AAAAAA',
                                alpha=0.6, zorder=1,
                                connectionstyle="arc3,rad=0.3")
    ax.add_patch(flow_arrow)

# Key insights - positioned outside main circle
# Insight 1: 80% Market Share
insight1_box = FancyBboxPatch((5, 8.5), 4, 0.9,
                              boxstyle="round,pad=0.15",
                              facecolor='#FFE5B4', edgecolor='#F9844A',
                              linewidth=2.5, alpha=0.95, zorder=10)
ax.add_patch(insight1_box)
ax.text(7, 9.1, '80% Market Share', ha='center', va='center',
       fontsize=10.5, weight='bold', color='#F9844A', zorder=11)
ax.text(7, 8.75, 'Medical Visa Processing', ha='center', va='center',
       fontsize=8, style='italic', color='#F9844A', zorder=11)

# Insight 2: Cultural Broker
insight2_box = FancyBboxPatch((-9, 8.5), 4, 0.9,
                              boxstyle="round,pad=0.15",
                              facecolor='#FFF9E6', edgecolor='#F9C74F',
                              linewidth=2.5, alpha=0.95, zorder=10)
ax.add_patch(insight2_box)
ax.text(-7, 9.1, 'Cultural Broker', ha='center', va='center',
       fontsize=10.5, weight='bold', color='#F9C74F', zorder=11)
ax.text(-7, 8.75, 'High Patient Loyalty', ha='center', va='center',
       fontsize=8, style='italic', color='#F9C74F', zorder=11)

# Title
title_box = FancyBboxPatch((-7.5, 9.5), 15, 0.6,
                          boxstyle="round,pad=0.1",
                          facecolor='#2E86AB', edgecolor='#1565C0',
                          linewidth=3, alpha=0.95, zorder=15)
ax.add_patch(title_box)
ax.text(0, 9.8, 'Figure 4: The "High-Touch" Patient Journey',
       ha='center', va='center', fontsize=16, weight='bold',
       color='white', zorder=16)

# Subtitle at bottom
ax.text(0, -8.8, 'Service Cycle: Comprehensive Patient Support from Mongolia to Taiwan',
       ha='center', va='center', fontsize=11, style='italic',
       color='#555555',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='#F5F5F5',
                edgecolor='#CCCCCC', linewidth=2))

# Add flow direction indicator
ax.text(0, -9.5, '→ Clockwise Flow →', ha='center', va='center',
       fontsize=9, color='#999999', style='italic')

# Save
plt.tight_layout()
plt.savefig('Figure4_High_Touch_Patient_Journey.png', dpi=300,
           bbox_inches='tight', facecolor='white', edgecolor='none')
plt.show()

print("✅ Figure 4 generated successfully!")
print("📁 Filename: 'Figure4_High_Touch_Patient_Journey.png'")
print("🔄 6-stage service cycle with no text overlap")
print("⭐ Key features highlighted: 80% Market Share & Cultural Broker")