import numpy as np
import matplotlib.pyplot as plt

# Stage 4: File input for multiple sets of data
file_name = "multiple_inputs.txt"

# Read data from file
with open(file_name, 'r') as file:
    lines = file.readlines()

# Process each set of inputs
for i, line in enumerate(lines):
    data = line.strip().split()
    a, b, c, x_start, x_end = map(float, data)
    x_start, x_end = int(x_start), int(x_end)

    # Generate x values and calculate y
    x = np.linspace(x_start, x_end, 100)
    y = a * x**2 + b * x + c

    # Plot the graph
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f"Set {i+1}", color='purple')
    plt.title(f"Weather Modeling - Stage 4: File Input (Set {i+1})")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"stage4_graph_set{i+1}.png")  # Save the graph
    plt.show()
