# Version 1: Hardcoded Values
import matplotlib.pyplot as plt
import numpy as np

# Hardcoded coefficients
a = 0.5
b = -3
c = 28

# Example time
t = 5
T = a * t**2 + b * t + c
print(f"Predicted temperature at t={t}: {T:.2f}°C")

# Graph over a range of times
times = np.linspace(0, 10, 100)
temps = a * times**2 + b * times + c

plt.figure(figsize=(8,5))
plt.plot(times, temps, label="Temperature Curve")
plt.scatter([t], [T], color="red", label=f"t={t}, T={T:.2f}°C")
plt.title("Version 1: Hardcoded Coefficients")
plt.xlabel("Time (t)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.savefig("version1_graph.png")
print("Graph saved as version1_graph.png")
