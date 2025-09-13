# ===== INCREMENTAL MODEL =====
import matplotlib.pyplot as plt
import numpy as np

print("=== INCREMENTAL MODEL ===")

# Quadratic weather model
def quadratic_weather_model(hour):
    a, b, c = -0.02, 0.5, 15
    return a * (hour ** 2) + b * hour + c

# Increments: gradually adding more predictions
increments = [ [0, 12, 24], [0, 6, 12, 18, 24], [0, 3, 6, 9, 12, 15, 18, 21, 24] ]
all_temps = []

for i, hours in enumerate(increments, start=1):
    print(f"Increment {i}:")
    temps = []
    for hour in hours:
        temp = quadratic_weather_model(hour)
        temps.append(temp)
        print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")
    print("---")
    all_temps.append((hours, temps))

# Plot
plt.figure(figsize=(8,5))
for i, (hours, temps) in enumerate(all_temps, start=1):
    plt.plot(hours, temps, marker='o', linestyle='-', label=f"Increment {i}")

plt.title("Incremental Model - Weather Prediction")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save graph
plt.savefig("incremental_graph.png")

print("\nGraph saved as 'incremental_graph.png' in your repository.")
