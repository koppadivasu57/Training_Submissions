import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample numeric data embedded in the script
df = pd.DataFrame({
    "Sales": np.random.randint(2000, 8000, 20),
    "Units": np.random.randint(50, 200, 20),
    "Cost": np.random.randint(1000, 6000, 20),
    "Profit": np.random.randint(500, 3000, 20)
})

# Calculate correlation matrix
corr = df.corr()

# Plot heatmap
plt.figure(figsize=(6, 5))
im = plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)

plt.title("Correlation Heatmap (Sample Sales Data)")
plt.colorbar(im)

# Axis ticks & labels
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)

# Annotate values
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        value = corr.iloc[i, j]
        plt.text(j, i, f"{value:.2f}", ha="center", va="center", color="black")

plt.tight_layout()
plt.show()
