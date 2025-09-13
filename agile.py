# ===== AGILE MODEL =====
import matplotlib.pyplot as plt
import numpy as np

print("=== AGILE MODEL ===")

# Quadratic weather model
def quadratic_weather_model(hour):
    a, b, c = -0.02, 0.5, 15
    return a * (hour ** 2) + b * hour + c

# Agile sprints
sprints = 2
times_to_check = [0, 6, 12, 18, 24]
all_temps = []

for sprint in range(1, sprints + 1):
    print(f"Sprint {sprint}:")
    temps = []
    for t in times_to_check:
        temp = quadratic_weather_model(t)
        temps.append(temp)
        print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
    print("---")
    all_temps.append(temps)

# Plot
plt.figure(figsize=(8,5))

for i, temps in enumerate(all_temps, start=1):
    plt.plot(times_to_check, temps, marker='o', linestyle='-', label=f"Sprint {i}")

plt.title("Agile Model - Weather Prediction")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save graph
plt.savefig("agile_graph.png")

print("\nGraph saved as 'agile_graph.png' in your repository.")
