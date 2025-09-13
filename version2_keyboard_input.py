# Version 2: Keyboard Input
import matplotlib.pyplot as plt
import numpy as np

# Get coefficients and time from user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
t = float(input("Enter time t (hour/day): "))

T = a * t**2 + b * t + c
print(f"Predicted temperature at t={t}: {T:.2f}°C")

# Graph
times = np.linspace(0, 10, 100)
temps = a * times**2 + b * times + c

plt.figure(figsize=(8,5))
plt.plot(times, temps, label="Temperature Curve")
plt.scatter([t], [T], color="red", label=f"t={t}, T={T:.2f}°C")
plt.title("Version 2: Keyboard Input")
plt.xlabel("Time (t)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.savefig("version2_graph.png")
print("Graph saved as version2_graph.png")
 