import matplotlib.pyplot as plt
import numpy as np

# Κατηγορίες (Άξονας Χ)
categories = ['0-5', '5-10', '10-11', '11-12', '12-13', '13-14', 
              '14-15', '15-16', '16-17', '17-18', '18-19', '19-20']

# --- ΕΔΩ ΠΕΡΑΣΕ ΤΑ ΠΟΣΟΣΤΑ ΑΠΟ ΤΟ CSV ΣΟΥ ---
data = {
    'Νεοελληνική Γλώσσα': [1.14, 6.72, 3.88, 6.03, 9.09, 13.02, 17.27, 17.33, 15.07, 8.15, 2.16, 0.13],
    'Φυσική': [18.52, 21.19, 3.33, 3.24, 3.55, 3.52, 3.75, 3.93, 4.83, 6.01, 8.60, 19.54],
    'Χημεία': [17.36, 25.70, 4.95, 4.65, 4.55, 4.75, 4.75, 5.26, 5.21, 6.33, 6.80, 9.68],
    'Βιολογία': [13.06, 21.72, 6.01, 6.61, 6.55, 6.67, 6.75, 6.35, 6.84, 6.92, 6.62, 5.89]
}

# --- NEON TERMINAL DESIGN SYSTEM ---
bg_color = '#05060A'       
text_color = '#E2E8F0'     
grid_color = '#1A1E29'     
base_color = '#3B82F6'     
accent_glow = '#00FFAA'    

plt.style.use('dark_background')
fig, axs = plt.subplots(2, 2, figsize=(16, 10))
fig.patch.set_facecolor(bg_color)

fig.suptitle('Κατανομή Βαθμολογιών | 3ο Πεδίο', 
             fontsize=22, fontweight='black', color='white', y=0.96)

# Watermark
fig.text(0.98, 0.02, '@Dimos Mossoras', fontsize=12, color="pink", alpha=0.3,
         ha='right', va='bottom', fontfamily='monospace', fontweight='bold')

axs = axs.flatten()
x_pos = np.arange(len(categories))

for i, (subject, percentages) in enumerate(data.items()):
    axs[i].set_facecolor(bg_color)
    
    max_idx = np.argmax(percentages)
    max_val = percentages[max_idx]
    
    for j, p in enumerate(percentages):
        is_max = (j == max_idx)
        current_color = accent_glow if is_max else base_color
        
        # Glow layers
        axs[i].plot([j, j], [0, p], color=current_color, linewidth=20, alpha=0.1, zorder=2, solid_capstyle='round')
        axs[i].plot([j, j], [0, p], color=current_color, linewidth=10, alpha=0.3, zorder=3, solid_capstyle='round')
        axs[i].plot([j, j], [0, p], color=current_color, linewidth=3, alpha=1.0, zorder=4, solid_capstyle='round')
        
        # Marker
        axs[i].scatter(j, p, color=current_color, 
                       s=180 if is_max else 60, 
                       edgecolors='white' if is_max else bg_color, 
                       linewidth=2, zorder=5)
        
        # Labels
        if p > 0.5:
            axs[i].annotate(f'{p:.1f}%',
                            xy=(j, p),
                            xytext=(0, 15 if is_max else 10), 
                            textcoords="offset points",
                            ha='center', va='bottom',
                            color=current_color if is_max else text_color, 
                            fontsize=11 if is_max else 9, 
                            fontweight='bold' if is_max else 'medium')

    for spine in axs[i].spines.values():
        spine.set_visible(False)
        
    axs[i].grid(axis='y', color=grid_color, linestyle='-', linewidth=1.5, zorder=1)
    axs[i].set_title(subject, fontsize=16, color='white', pad=20, fontweight='bold')
    axs[i].set_xticks(x_pos)
    axs[i].set_xticklabels(categories, rotation=45, ha='right', color='#94A3B8', fontsize=10, fontweight='bold')
    axs[i].tick_params(axis='x', colors=grid_color, length=0, pad=10) 
    axs[i].tick_params(axis='y', colors='#475569', labelsize=10, length=0) 
    axs[i].set_xticklabels(categories, rotation=45, ha='right', color='#94A3B8', fontsize=10, fontweight='bold')
    
    axs[i].set_ylim(0, max_val * 1.25)

plt.subplots_adjust(hspace=0.5, wspace=0.1)
plt.show()