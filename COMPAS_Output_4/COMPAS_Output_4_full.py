# coding: utf-8
import h5py
import pandas as pd
import matplotlib.pyplot as plt

# Open the HDF5 file
with h5py.File('COMPAS_Output_4.h5', 'r') as f:
    # List all groups and datasets
    print("Keys: %s" % f.keys())
    
    # Replace 'dataset_name' with the actual name of the dataset
    data = f['dataset_name'][:]

# Convert the data to a pandas DataFrame (if applicable)
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())
import h5py

# Open the HDF5 file
with h5py.File('COMPAS_Output_4.h5', 'r') as f:
    # List all groups and datasets
    def print_attrs(name, obj):
        print(name)
    f.visititems(print_attrs)
    
import h5py
import pandas as pd
import matplotlib.pyplot as plt

# Open the HDF5 file
with h5py.File('COMPAS_Output_4.h5', 'r') as f:
    # List all groups and datasets
    print("Keys: %s" % f.keys())
    
    # Replace 'dataset_name' with the actual name of the dataset
    data = f['BSE_System_Parameters'][:]

# Convert the data to a pandas DataFrame (if applicable)
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())
import h5py
import pandas as pd
import matplotlib.pyplot as plt

# Open the HDF5 file
with h5py.File('COMPAS_Output_4.h5', 'r') as f:
    # List all groups and datasets
    print("Keys: %s" % f.keys())
    
    # List the contents of the 'BSE_System_Parameters' group
    group = f['BSE_System_Parameters']
    print("Contents of 'BSE_System_Parameters': %s" % group.keys())
    
    # Replace 'dataset_name' with the actual name of the dataset within the group
    data = group['dataset_name'][:]

# Convert the data to a pandas DataFrame (if applicable)
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())
import h5py
import pandas as pd
import matplotlib.pyplot as plt

# Open the HDF5 file
with h5py.File('COMPAS_Output_4.h5', 'r') as f:
    # List all groups and datasets
    print("Keys: %s" % f.keys())
    
    # List the contents of the 'BSE_System_Parameters' group
    group = f['BSE_System_Parameters']
    print("Contents of 'BSE_System_Parameters': %s" % group.keys())
    
    # Replace 'dataset_name' with the actual name of the dataset within the group
    data = group['Eccentricity@ZAMS'][:]

# Convert the data to a pandas DataFrame (if applicable)
df = pd.DataFrame(data, columns=['Eccentricity@ZAMS'])

# Display the first few rows of the DataFrame
print(df.head())

# Example: Plotting data (if applicable)
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Eccentricity@ZAMS'])
plt.title('Eccentricity at ZAMS')
plt.xlabel('Index')
plt.ylabel('Eccentricity')
plt.show()
