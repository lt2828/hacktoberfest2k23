import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Generate sample georeferenced data (longitude, latitude, and values)
lon = np.linspace(-180, 180, 360)
lat = np.linspace(-90, 90, 180)
lon, lat = np.meshgrid(lon, lat)
data = np.sin(np.radians(lat))

# Create a figure and axis with a specified map projection (e.g., PlateCarree)
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})

# Plot the georeferenced data
c = ax.contourf(lon, lat, data, levels=30, transform=ccrs.PlateCarree(), cmap='viridis')

# Add coastlines and gridlines
ax.coastlines()
ax.gridlines()

# Add a colorbar
cbar = plt.colorbar(c, ax=ax, orientation='vertical', shrink=0.8, pad=0.05)
cbar.set_label('Data Values')

# Set the title
ax.set_title('Georeferenced Data Plot')

# Show the plot
plt.show()
