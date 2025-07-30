import folium
from datetime import datetime

def simulate_gps():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"GPS coordinates spoofed at {current_time}")
    # Example coordinates (New York)
    latitude, longitude = 40.7128, -74.0060
    m = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker([latitude, longitude], tooltip="Target Location").add_to(m)
    m.save("output/gps_map.html")
    print("GPS map saved to output/gps_map.html")