import numpy as np
import matplotlib.pyplot as plt

# Generate data for bell curve
mu = 0  # Mean of the normal distribution
sigma = 1  # Standard deviation of the normal distribution
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)  # Generate 1000 data points
y = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)  # Calculate corresponding y values

# Plot bell curve
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='b', linewidth=2)
plt.title('Bell Curve (Normal Distribution)')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()
