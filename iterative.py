import matplotlib.pyplot as plt
import numpy as np

def quadratic_weather_model(t):
    return 0.1 * t**2 - 1.2 * t + 25

print("\n=== ITERATIVE MODE ===")
iterations = {}
for iteration in range(1, 4):
    print(f"Iteration {iteration}:")
    hours = list(range(0, 25, 12))  # 0,12,24
    temps = [quadratic_weather_model(h) for h in hours]
    iterations[iteration] = (hours, temps)
    for h, T in zip(hours, temps):
        print(f"Time: {h} hrs -> Temp: {T:.2f}°C")
    print("---")

# Graph
plt.figure(figsize=(8,5))
for i, (hours, temps) in iterations.items():
    plt.plot(hours, temps, marker="o", label=f"Iteration {i}")

plt.title("Iterative Model (Multiple Cycles with Updates)")
plt.xlabel("Time (hrs)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("iterative_graph.png")
print("Graph saved as iterative_graph.png")
