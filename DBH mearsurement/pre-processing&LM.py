import laspy
import numpy as np
from scipy.optimize import least_squares
import matplotlib.pyplot as plt
import argparse

# Set up command line argument parsing
parser = argparse.ArgumentParser(description="Calculate DBH from a LAS point cloud file.")
parser.add_argument("file_path", type=str, help="Path to the LAS point cloud file.")
args = parser.parse_args()

# Load LAS point cloud data from the provided file path
las = laspy.read(args.file_path)

# Extract the XYZ coordinates from the point cloud
points = np.vstack((las.x, las.y, las.z)).transpose()

# Get the minimum Z value
min_z = np.min(points[:, 2])

# Subtract the minimum Z value from all Z coordinates to set the lowest point to 0 meters
points[:, 2] -= min_z

# Print the adjusted height range
print(f"Adjusted height range: {points[:, 2].min()} to {points[:, 2].max()} meters")

# Filter points within the target breast height range (1.35 meters to 1.38 meters)
target_height_mask = (points[:, 2] > 1.35) & (points[:, 2] < 1.38)
target_height_points = points[target_height_mask]

# Check if there are enough points within the target height range
if target_height_points.shape[0] == 0:
    print("No points found in the target height range. Please check your data and height range.")
    exit()

# Extract the XY coordinates of the points at the target height
xy_points = target_height_points[:, :2]

# Define the model function for the circle
def circle_residuals(params, x, y):
    xc, yc, r = params
    return (x - xc)**2 + (y - yc)**2 - r**2

# Initial guess for the circle's center and radius
x_mean, y_mean = np.mean(xy_points[:, 0]), np.mean(xy_points[:, 1])
r_guess = np.mean(np.sqrt((xy_points[:, 0] - x_mean)**2 + (xy_points[:, 1] - y_mean)**2))
initial_guess = [x_mean, y_mean, r_guess]

# Fit a circle using the Levenberg–Marquardt algorithm
result = least_squares(circle_residuals, initial_guess, args=(xy_points[:, 0], xy_points[:, 1]))

# Extract the fitted circle's center and radius
xc, yc, r = result.x
circle_center = np.array([xc, yc])
circle_radius = r

# Calculate the DBH (Diameter at Breast Height)
dbh = 2 * circle_radius

print(f"Calculated DBH: {dbh:.5f} meters")

# Plot the point cloud and the fitted circle
plt.scatter(xy_points[:, 0], xy_points[:, 1], color='grey', s=1, label='Data Points')
plt.scatter(circle_center[0], circle_center[1], color='green', s=100, label='Circle Center')

# Draw the fitted circle
circle = plt.Circle(circle_center, circle_radius, color='green', fill=False, label='Fitted Circle')
plt.gca().add_artist(circle)

plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='lower left')
plt.title('Circle Fitting at 1.35-1.38m Height using Levenberg–Marquardt Algorithm')
plt.show()
