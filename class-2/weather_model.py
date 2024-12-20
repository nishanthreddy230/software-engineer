import numpy as np
import matplotlib.pyplot as plt

# Stage 2: Keyboard input
print("Enter the coefficients for the quadratic equation (y = ax^2 + bx + c):")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter constant c: "))

# Define the range for x
x_start = int(input("Enter the start value for x: "))
x_end = int(input("Enter the end value for x: "))
x = np.linspace(x_start, x_end, 100)  # Generate 100 points between x_start and x_end

# Calculate y using the quadratic formula
y = a * x**2 + b * x + c

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Predicted Output", color='green')
plt.title("Weather Modeling - Stage 2: Keyboard Input")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig("stage2_graph.png")  # Save the graph
plt.show()
