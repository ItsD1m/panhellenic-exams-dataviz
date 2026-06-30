import matplotlib.pyplot as plt
import numpy as np

# Κατηγορίες (Άξονας Χ)
categories = ['0-5', '5-10', '10-11', '11-12', '12-13', '13-14', 
              '14-15', '15-16', '16-17', '17-18', '18-19', '19-20']

# Τα Διορθωμένα Δεδομένα 
data = {
    'Νεοελληνική Γλώσσα': [3.28, 20.64, 9.69, 11.97, 14.20, 14.01, 11.93, 8.24, 4.11, 1.66, 0.26, 0.01],
    'Μαθηματικά': [38.08, 25.99, 5.36, 5.31, 5.10, 4.82, 4.30, 3.83, 2.84, 1.88, 1.43, 1.05],
    'Πληροφορική': [18.58, 22.55, 4.63, 4.55, 4.55, 4.63, 4.99, 5.47, 6.07, 7.56, 7.92, 8.49],
    'Οικονομία': [25.09, 23.00, 4.84, 4.51, 4.32, 4.30, 4.37, 4.43, 5.19, 5.74, 6.45, 7.77]
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

fig.suptitle('Κατανομή Βαθμολογιών | 4ο Πεδίο', 
             fontsize=22, fontweight='black', color='white', y=0.96)

# Το Watermark
fig.text(0.98, 0.02, '@Dimos Mossoras', fontsize=12, color="pink", alpha=0.3,
         ha='right', va='bottom', fontfamily='monospace', fontweight='bold')

axs = axs.flatten()
x_pos = np.arange(len(categories))

for i, (subject, percentages) in enumerate(data.items()):
    axs[i].set_facecolor(bg_color)
    
    max_idx = np.argmax(percentages)
    max_val = percentages[max_idx]
    
    # Layering για το Neon Effect
    for j, p in enumerate(percentages):
        is_max = (j == max_idx)
        current_color = accent_glow if is_max else base_color
        
        # Outer Glow 
        axs[i].plot([j, j], [0, p], color=current_color, linewidth=20, alpha=0.1, zorder=2, solid_capstyle='round')
        # Inner Glow 
        axs[i].plot([j, j], [0, p], color=current_color, linewidth=10, alpha=0.3, zorder=3, solid_capstyle='round')
        # Core 
        axs[i].plot([j, j], [0, p], color=current_color, linewidth=3, alpha=1.0, zorder=4, solid_capstyle='round')
        
        # Marker Κορυφής
        axs[i].scatter(j, p, color=current_color, 
                       s=180 if is_max else 60, 
                       edgecolors='white' if is_max else bg_color, 
                       linewidth=2, zorder=5)
        
        # Data Labels
        if p > 0.5:
            lbl_weight = 'bold' if is_max else 'medium'
            lbl_size = 11 if is_max else 9
            
            axs[i].annotate(f'{p:.1f}%',
                            xy=(j, p),
                            xytext=(0, 15 if is_max else 10), 
                            textcoords="offset points",
                            ha='center', va='bottom',
                            color=current_color if is_max else text_color, 
                            fontsize=lbl_size, fontweight=lbl_weight)

    for spine in axs[i].spines.values():
        spine.set_visible(False)
        
    axs[i].grid(axis='y', color=grid_color, linestyle='-', linewidth=1.5, zorder=1)
    
    axs[i].set_title(subject, fontsize=16, color='white', pad=20, fontweight='bold')
    
    axs[i].set_xticks(x_pos)
    axs[i].set_xticklabels(categories, rotation=45, ha='right', color="#FDFDFD", fontsize=10, fontweight='bold')
    axs[i].tick_params(axis='x', colors=grid_color, length=0, pad=10) 
    axs[i].tick_params(axis='y', colors='#475569', labelsize=10, length=0) 
    axs[i].set_xticklabels(categories, rotation=45, ha='right', color='#94A3B8', fontsize=10, fontweight='bold')
    
    axs[i].set_ylim(0, max_val * 1.25)

plt.subplots_adjust(hspace=0.5, wspace=0.1)
plt.show()