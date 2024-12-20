import numpy as np
import matplotlib.pyplot as plt

# Stage 1: Hardcoded coefficients and input
# Quadratic equation: y = ax^2 + bx + c
a = 0.01  # Coefficient for x^2
b = -0.5  # Coefficient for x
c = 30    # Constant term

# Generate x values (e.g., days of the year)
x = np.linspace(1, 365, 365)  # Days from 1 to 365
y = a * x**2 + b * x + c      # Calculate y using the quadratic formula

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Predicted Temperature (°C)", color='blue')
plt.title("Weather Modeling - Stage 1: Hardcoded Input")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.savefig("stage1_graph.png")  # Save the graph
plt.show()
