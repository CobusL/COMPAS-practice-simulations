# coding: utf-8
import h5py
import pandas as pd
import matplotlib.pyplot as plt

# Open the HDF5 file
file_path = 'COMPAS_Output_5.h5'
with h5py.File(file_path, 'r') as f:
    # List all groups and datasets
    print("Keys: %s" % f.keys())
    
    # List the contents of the 'BSE_System_Parameters' group
    group = f['BSE_System_Parameters']
    print("Contents of 'BSE_System_Parameters': %s" % group.keys())
    
    # Extract data from the 'Eccentricity@ZAMS' dataset
    eccentricity = group['Eccentricity@ZAMS'][:]

# Convert the data to a pandas DataFrame
df = pd.DataFrame({
    'Eccentricity@ZAMS': eccentricity
})

# Display the first few rows of the DataFrame
print(df.head())

# Check the unique values and their counts
unique_values = df['Eccentricity@ZAMS'].value_counts()
print("Unique values and their counts:\n", unique_values)

# Calculate and print statistics
min_value = df['Eccentricity@ZAMS'].min()
max_value = df['Eccentricity@ZAMS'].max()
mean_value = df['Eccentricity@ZAMS'].mean()
std_value = df['Eccentricity@ZAMS'].std()

print(f"Min: {min_value}")
print(f"Max: {max_value}")
print(f"Mean: {mean_value}")
print(f"Standard Deviation: {std_value}")

# Plot the distribution of Eccentricity@ZAMS with more bins
plt.figure(figsize=(10, 6))
plt.hist(df['Eccentricity@ZAMS'], bins=50, edgecolor='k')
plt.title('Distribution of Eccentricity at ZAMS')
plt.xlabel('Eccentricity@ZAMS')
plt.ylabel('Frequency')
plt.show()

# Plot a box plot of Eccentricity@ZAMS
plt.figure(figsize=(10, 6))
plt.boxplot(df['Eccentricity@ZAMS'], vert=False)
plt.title('Box Plot of Eccentricity at ZAMS')
plt.xlabel('Eccentricity@ZAMS')
plt.show()
