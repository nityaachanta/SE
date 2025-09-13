import matplotlib.pyplot as plt
import numpy as np

def quadratic_weather_model(t):
    return 0.1 * t**2 - 1.2 * t + 25

print("=== WATERFALL MODE ===")
hours = list(range(0, 25, 6))  # 0,6,12,18,24
temps = [quadratic_weather_model(h) for h in hours]

for h, T in zip(hours, temps):
    print(f"Time: {h} hrs -> Predicted Temp: {T:.2f}°C")

# Graph
plt.figure(figsize=(8,5))
plt.plot(hours, temps, marker="o", label="Waterfall Cycle")
plt.title("Waterfall Model (One Sequential Cycle)")
plt.xlabel("Time (hrs)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("waterfall_graph.png")
print("Graph saved as waterfall_graph.png")

