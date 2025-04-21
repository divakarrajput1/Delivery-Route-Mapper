import folium # a Python library based on Leaflet.js.
import pandas as pd

# Read the geocoded data from CSV
df = pd.read_csv("delivery_points_geocoded.csv")

# Create a map centered around Bangalore (you can adjust lat/lon)
m = folium.Map(location=[12.9716, 77.5946], zoom_start=12)

# Loop through each row in the CSV and plot it on the map
for i, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"{row['name']} - {row['address']}",  # Show name and address on click
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# Save the map to an HTML file
m.save("delivery_map.html")

print("Map has been saved as 'delivery_map.html'")
