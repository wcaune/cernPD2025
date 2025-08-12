import h5py as h5
import matplotlib.pyplot as plt

# Load the point cloud data from the HDF5 file
entry = 0
with h5.File('example_xyze_100.h5','r') as f:
    print(len(f['data']),'images found')
    # read the specified entry
    pts=f['data'][entry].reshape(-1,4)

print('Visualizing entry',entry)

# Create a new figure and a 3D axes object
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(pts[:,0], pts[:,1], pts[:,2], s=2)

# Set labels for axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Display the plot
plt.show()
