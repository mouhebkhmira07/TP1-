import matplotlib.pyplot as plt
import numpy as np

# Data from experiments
experiences = ['Experience 1', 'Experience 2', 'Moyenne', 'Experience 3']
huile_15W40 = [0.837, 0.844, 0.84, 0.88]
detergent = [1.056, 1.019, 1.035, 1.02]
liquide_inconnu = [0.923, 0.999, 0.961, np.nan]  # np.nan for missing data

# Create the plot
plt.figure(figsize=(12, 8))

# Plot curves for each liquid
plt.plot(experiences, huile_15W40, 'o-', linewidth=3, markersize=10, 
         label='Huile 15W40', color='#FF6B6B', markerfacecolor='white', markeredgewidth=2)

plt.plot(experiences, detergent, 's-', linewidth=3, markersize=10, 
         label='Detergent', color='#4ECDC4', markerfacecolor='white', markeredgewidth=2)

plt.plot(experiences[:3], liquide_inconnu[:3], '^-', linewidth=3, markersize=10, 
         label='Liquide Inconnu', color='#45B7D1', markerfacecolor='white', markeredgewidth=2)

# Add reference line for water
plt.axhline(y=1.0, color='red', linestyle='--', linewidth=2, alpha=0.7, label='Eau (d=1.000)')

# Customize the plot
plt.xlabel('Experiences', fontsize=14, fontweight='bold')
plt.ylabel('Densite', fontsize=14, fontweight='bold')
plt.title('Courbes de Densite des Liquides', fontsize=16, fontweight='bold', pad=20)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Add value annotations on points
for i, (h_val, d_val, l_val) in enumerate(zip(huile_15W40, detergent, liquide_inconnu)):
    plt.annotate(f'{h_val:.3f}', (i, h_val), textcoords="offset points", 
                xytext=(0,15), ha='center', fontsize=9, fontweight='bold', color='#FF6B6B')
    plt.annotate(f'{d_val:.3f}', (i, d_val), textcoords="offset points", 
                xytext=(0,15), ha='center', fontsize=9, fontweight='bold', color='#4ECDC4')
    if not np.isnan(l_val):
        plt.annotate(f'{l_val:.3f}', (i, l_val), textcoords="offset points", 
                    xytext=(0,-20), ha='center', fontsize=9, fontweight='bold', color='#45B7D1')

plt.tight_layout()
plt.savefig('courbes_densite.png', dpi=300, bbox_inches='tight')
plt.show()
