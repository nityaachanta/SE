# Version 4: File Input (Multiple Sets)
import matplotlib.pyplot as plt
import numpy as np

all_times = []
all_temps = []

with open("inputs_multiple.txt", "r") as f:
    for line in f:
        a, b, c, t = map(float, line.strip().split())
        T = a * t**2 + b * t + c
        print(f"a={a}, b={b}, c={c}, t={t} -> T={T:.2f}°C")

        # Store curve and point for plotting
        times = np.linspace(0, 10, 100)
        temps = a * times**2 + b * times + c
        all_times.append((times, t))
        all_temps.append((temps, T))

# Plot all sets
plt.figure(figsize=(8,5))
for i, ((times, t), (temps, T)) in enumerate(zip(all_times, all_temps), start=1):
    plt.plot(times, temps, label=f"Set {i}")
    plt.scatter([t], [T], label=f"Set {i}: t={t}, T={T:.2f}°C")

plt.title("Version 4: File Input (Multiple Sets)")
plt.xlabel("Time (t)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.savefig("version4_graph.png")
print("Graph saved as version4_graph.png")
