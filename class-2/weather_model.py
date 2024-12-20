import numpy as np
import matplotlib.pyplot as plt

# Stage 3: File input for a single set of data
file_name = "single_input.txt"

# Read data from file
with open(file_name, 'r') as file:
    lines = file.readlines()
    a = float(lines[0].strip())
    b = float(lines[1].strip())
    c = float(lines[2].strip())
    x_start = int(lines[3].strip())
    x_end = int(lines[4].strip())

# Generate x values and calculate y
x = np.linspace(x_start, x_end, 100)
y = a * x**2 + b * x + c

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Predicted Output", color='orange')
plt.title("Weather Modeling - Stage 3: File Input (Single Set)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig("stage3_graph.png")  # Save the graph
plt.show()
