
PROFILE_FILE = 'MtDH.profile'
OUTPUT_IMAGE = 'MtDH_dope_profile.png'
TITLE        = 'DOPE profile — MtDH model 2'

import matplotlib.pyplot as plt

residues, scores = [], []
with open(PROFILE_FILE) as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        residues.append(int(parts[0]))
        scores.append(float(parts[-1]))   # нормированный DOPE — в последней колонке

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(residues, scores, linewidth=1, color='tab:blue')
ax.axhline(0, color='gray', linestyle='--', linewidth=0.5)
ax.set_xlabel('Residue number')
ax.set_ylabel('Normalized DOPE score')
ax.set_title(TITLE)
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(OUTPUT_IMAGE, dpi=150)
plt.show()