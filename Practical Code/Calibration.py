import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Theoretical and experimental frequencies
theoretical = np.array([2000, 8000, 32000, 50000])
experimental = np.array([2062, 8312, 33260, 52000])

# Define the model function for the chi-squared fit
def model_function(theoretical, a, b):
    return a * theoretical + b

# Perform chi-squared fit
params, covariance = curve_fit(model_function, theoretical, experimental)

# Get the parameters of the fitted line
a, b = params

# Plot residuals and the fitted line side by side
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# Plot residuals
residuals = experimental - model_function(theoretical, a, b)
axs[1].scatter(theoretical, residuals, color='black', alpha=0.7)
axs[1].axhline(0, color='red', linestyle='--', linewidth=2)  # Add a horizontal line at y=0 for reference
axs[1].set_xlabel('Theoretical Frequency [Hz]')
axs[1].set_ylabel('Residuals [Hz]')
axs[1].set_title('Residuals of Chi-squared Fit')
axs[1].grid(True)
# Plot the fitted line
axs[0].scatter(theoretical, experimental, color='black', alpha=0.7)
axs[0].plot(theoretical, model_function(theoretical, a, b), color='red', linewidth=2)
axs[0].set_xlabel('Theoretical Frequency [Hz]')
axs[0].set_ylabel('Experimental Frequency [Hz]')
axs[0].set_title('Linear Fit of Theoretical and Experimental Frequencies')
axs[0].grid(True)
# Print the line equation
equation = f'Experimental: {a:.3f} * Theoretical  {b:.2f}'
axs[0].annotate(equation, xy=(0.05, 0.9), xycoords='axes fraction', fontsize=9, color='black')

plt.show()
