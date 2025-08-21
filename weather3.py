# Weather Modeling using Quadratic Equation
# Stage 3: Read from file (single set of inputs)

# Open the input file
with open("input.txt", "r") as f:
    data = f.read().split()  # Read and split by spaces
    a, b, c, t = map(float, data)  # Convert to numbers

# Calculate T(t) = at^2 + bt + c
T = a * t * t + b * t + c

# Show result
print("Stage 3: File Input (Single Set)")
print(f"Inputs: a={a}, b={b}, c={c}, t={t}")
print(f"Predicted Temperature T({t}) = {T}")
