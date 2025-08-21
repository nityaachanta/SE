# Weather Modeling using Quadratic Equation
# Stage 4: Read from file (multiple sets of inputs)

# Open the input file
with open("input2.txt", "r") as f:
    lines = f.readlines()  # Read all lines

print("Stage 4: File Input (Multiple Sets)\n")

# Loop through each line
for i, line in enumerate(lines, start=1):
    # Split values in the line
    data = line.strip().split()
    if len(data) == 4:  # Ensure correct format
        a, b, c, t = map(float, data)
        # Calculate T(t)
        T = a * t * t + b * t + c
        # Show result
        print(f"Set {i}: a={a}, b={b}, c={c}, t={t}")
        print(f"Predicted Temperature T({t}) = {T}\n")
    else:
        print(f"Skipping line {i}, invalid format: {line}")
