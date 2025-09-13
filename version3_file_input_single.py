# Version 3: File Input (Single Set)
import matplotlib.pyplot as plt
import numpy as np

# Read values from file
with open("inputs_single.txt", "r") as f:
    lines = f.readlines()

a = float(lines[0])
b = float(lines[1])
c = float(lines[2])
t = float(lines[3])

T = a * t**2 + b * t + c
print(f"Predicted temperature at t={t}: {T:.2f}°C")

# Graph
times = np.linspace(0, 10, 100)
temps = a * times**2 + b * times + c

plt.figure(figsize=(8,5))
plt.plot(times, temps, label="Temperature Curve")
plt.scatter([t], [T], color="red", label=f"t={t}, T={T:.2f}°C")
plt.title("Version 3: File Input (Single Set)")
plt.xlabel("Time (t)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.savefig("version3_graph.png")
print("Graph saved as version3_graph.png")
