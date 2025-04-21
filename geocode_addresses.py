import pandas as pd
from geopy.geocoders import Nominatim # free geocoding API.
import time

# Talk to the map genie
geolocator = Nominatim(user_agent="map-project")

# Read your CSV
df = pd.read_csv("delivery_points.csv")

# Make space for the map dots
df["latitude"] = None
df["longitude"] = None

# Go one by one and ask the genie: "Where is this place?"
for i, row in df.iterrows():
    try:
        location = geolocator.geocode(row["address"])
        if location:
            df.at[i, "latitude"] = location.latitude
            df.at[i, "longitude"] = location.longitude
            print(f"{row['name']} → {location.latitude}, {location.longitude}")
        else:
            print(f"Couldn't find: {row['address']}")
    except Exception as e:
        print(f"Oops! Something went wrong: {e}")

    time.sleep(1)  # Don't ask too fast!

# Save your new treasure map
df.to_csv("delivery_points_geocoded.csv", index=False)
print("✅ Done! Check your new file: delivery_points_geocoded.csv")
