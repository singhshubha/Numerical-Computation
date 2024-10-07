import math
import matplotlib.pyplot as plt

# Function to calculate the value of f(x)
def func(x):
    """Returns the value of e^x for the given x."""
    return math.exp(x)

# Function to compute the derivative using the five-point formula
def five_point_derivative(values, idx, step_size):
    """Applies the five-point formula to estimate the derivative at index idx."""
    return (1 / (12 * step_size)) * (values[idx - 2] - 8 * values[idx - 1] + 8 * values[idx + 1] - values[idx + 2])

# Function to compute the derivative at the start using the start-point formula
def start_point_derivative(values, idx, step_size):
    """Uses the start-point formula to approximate the derivative for the first two indices."""
    return (1 / (12 * step_size)) * (
        -25 * values[idx + 0]
        + 48 * values[idx + 1]
        - 36 * values[idx + 2]
        + 16 * values[idx + 3]
        - 3 * values[idx + 4]
    )

# Function to compute the derivative at the end using the end-point formula
def end_point_derivative(values, idx, step_size):
    """Uses the end-point formula to approximate the derivative for the last two indices."""
    return (1 / (12 * step_size)) * (
        -25 * values[idx]
        + 48 * values[idx - 1]
        - 36 * values[idx - 2]
        + 16 * values[idx - 3]
        - 3 * values[idx - 4]
    )

# Function to derive the set of derivatives for given x values and function values
def approximate_derivatives(x_values, f_values):
    """Calculates the derivative values for the given set of x and f(x), assuming there are 5 or more points."""
    num_points = len(x_values)
    step_size = x_values[1] - x_values[0]
    derivative_values = []

    # Compute derivatives at the start points
    derivative_values.append(start_point_derivative(f_values, 0, step_size))
    derivative_values.append(start_point_derivative(f_values, 1, step_size))

    # Compute derivatives at midpoint using five-point formula
    for idx in range(2, num_points - 2):
        derivative_values.append(five_point_derivative(f_values, idx, step_size))

    # Compute derivatives at end points
    derivative_values.append(end_point_derivative(f_values, num_points - 2, step_size))
    derivative_values.append(end_point_derivative(f_values, num_points - 1, step_size))

    return derivative_values

# Test data for points 2.1, 2.2, ..., 2.7
test_points = [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7]
test_f_points = [-1.709847, -1.373823, -1.119214, -0.9160143, -0.7470223, -0.6015966, -0.5123467]

# Compute approximate derivatives for test points
computed_derivatives = approximate_derivatives(test_points, test_f_points)

# Display the computed derivatives
print("Computed Derivatives for Test Points:")
for i in range(len(test_points)):
    print(f"Point: {test_points[i]}, Computed Derivative: {computed_derivatives[i]}")

# Define and compute approximations for different values of n
points_data = []
for n in [11, 21, 41]:
    step_size = 2 / (n - 1)
    x_range = [-1 + i * step_size for i in range(n)]

    f_values = [func(x) for x in x_range]
    derived_values = approximate_derivatives(x_range, f_values)
    error_values = [abs(func(x) * ((step_size ** 4) / 30)) for x in x_range]  # Calculate approximation errors

    points_data.append((x_range, derived_values, error_values))

    # Print the results
    print("\nx, f(x), f'(x) approx, Error: R(x)")
    for i in range(len(x_range)):
        print(f"{x_range[i]}, {round(f_values[i], 5)}, {round(derived_values[i], 5)}, {round(error_values[i], 8)}")

# Plotting f'(x) approximations with modified appearance
plt.figure(figsize=(12, 6))

# Define a color palette and markers for distinction
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
markers = ['o', 's', 'D']
labels = ["11 points", "21 points", "41 points"]

# Plotting approximations
for idx, (x_range, derived_values, _) in enumerate(points_data):
    plt.plot(
        x_range, derived_values,
        color=colors[idx],
        linestyle='-',
        linewidth=2,
        marker=markers[idx],
        markersize=6,
        label=f"{labels[idx]}"
    )

# Adding labels, title, and grid
plt.xlabel("X-axis", fontsize=14)
plt.ylabel("f'(x) Approximation", fontsize=14)
plt.title("Approximations of f'(x) for Different Number of Points", fontsize=16, fontweight='bold')
plt.legend(title="Approximation Points", fontsize=12, title_fontsize=12)
plt.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.7)
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)  # Add a horizontal reference line at y = 0
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)  # Add a vertical reference line at x = 0

plt.tight_layout()
plt.show()

# Plotting the error values for each n with modified appearance
plt.figure(figsize=(12, 6))
for idx, (x_range, _, error_values) in enumerate(points_data):
    plt.plot(
        x_range, error_values,
        color=colors[idx],
        linestyle='-',
        linewidth=2,
        marker=markers[idx],
        markersize=5,
        label=f"{labels[idx]}"
    )

plt.xlabel("X-axis", fontsize=12)
plt.ylabel("Error in f'(x) Approximation", fontsize=12)
plt.title("Error Analysis for f'(x) Approximations", fontsize=14, fontweight='bold')
plt.legend(title="Approximation Points", fontsize=10, title_fontsize=10)
plt.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.7)
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)

plt.tight_layout()
plt.show()
