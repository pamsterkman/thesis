import matplotlib.pyplot as plt
import laspy

# Read LAZ file lazily
las = laspy.read("C:\\Data_thesis_pam\\pc_t2.las")

# Extract Z values
z_values = las.z

# Filter Z values below 20
filtered_z_values = z_values[z_values < 15]

# Create a histogram
plt.hist(filtered_z_values, bins=30, color='blue', edgecolor='black')

# Customize the plot
plt.title('Histogram of Z Values')
plt.xlabel('Z Values')
plt.ylabel('Frequency')

# Show the plot
plt.show()

