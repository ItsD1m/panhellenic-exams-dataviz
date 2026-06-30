import matplotlib.pyplot as plt
import numpy as np

# Κατηγορίες (Άξονας Χ)
categories = ['0-5', '5-10', '10-11', '11-12', '12-13', '13-14', 
              '14-15', '15-16', '16-17', '17-18', '18-19', '19-20']

# Τα Δεδομένα (1ο Πεδίο - ΓΕΛ Ημερήσια) 
data = {

    'Νεοελληνική Γλώσσα': [1.84, 13.19, 6.63, 8.46, 11.27, 13.94, 14.94, 13.24, 10.10, 4.88, 1.43, 0.09],
    'Αρχαία Ελληνικά': [14.82, 40.85, 8.15, 7.60, 6.34, 5.66, 4.80, 4.40, 3.20, 2.67, 1.32, 0.19],
    'Ιστορία': [26.04, 26.07, 4.42, 4.36, 4.45, 4.18, 3.95, 3.77, 4.23, 4.86, 6.73, 6.96],
    'Λατινικά': [17.88, 17.10, 4.07, 4.18, 4.66, 4.85, 5.30, 5.58, 6.34, 7.39, 9.34, 13.31]
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

fig.suptitle('Κατανομή Βαθμολογιών | 1ο Πεδίο', 
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
    axs[i].tick_params(axis='x', colors=grid_color, length=0, pad=10) 
    axs[i].tick_params(axis='y', colors='#475569', labelsize=10, length=0) 
    axs[i].set_xticklabels(categories, rotation=45, ha='right', color='#94A3B8', fontsize=10, fontweight='bold')
    
    axs[i].set_ylim(0, max_val * 1.25)

plt.subplots_adjust(hspace=0.5, wspace=0.1)
plt.show()