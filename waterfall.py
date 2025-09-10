# ===== WATERFALL MODEL =====
import matplotlib.pyplot as plt
import numpy as np

print("=== WATERFALL MODEL ===")

# Plan -> Develop -> Test -> Deliver (one cycle)
def quadratic_weather_model(hour):
    # Example quadratic model: temp = a*hour² + b*hour + c
    a, b, c = -0.02, 0.5, 15   # coefficients (adjust as needed)
    return a * (hour ** 2) + b * hour + c

# Hours (every 6 hrs)
hours = np.arange(0, 25, 6)
temps = []

# Predictions
for hour in hours:
    temp = quadratic_weather_model(hour)
    temps.append(temp)
    print(f"Time: {hour} hrs -> Predicted Temp: {temp:.2f}°C")

# Plot the graph
plt.figure(figsize=(8,5))
plt.plot(hours, temps, marker='o', linestyle='-', color='b', label="Predicted Temp")
plt.title("Waterfall Model - Weather Prediction")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()
