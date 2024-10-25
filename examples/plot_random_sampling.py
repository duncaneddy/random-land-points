"""
This is a simple example that shows how to create a plot of a country outline.
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs

import random_land_points as rlp

# Get the country polygon
country = 'United States of America'
polygon = rlp.get_country_points(country)

# Create the plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# Set background plot
ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())
ax.stock_img()

# Sample 10 random points in the United States
points = rlp.random_points('United States of America', count=10)

# Plot the points
ax.scatter(points[:, 0], points[:, 1], transform=ccrs.PlateCarree(), color='blue', s=10)

# Sample 10 random points in the United States
points = rlp.random_points('Norway', count=10)

# Plot the points
ax.scatter(points[:, 0], points[:, 1], transform=ccrs.PlateCarree(), color='red', s=10)

ax.set_title('Random Points')
plt.show()