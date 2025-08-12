import json
import random
import time

# Number of buses
bus_ids = ["Bus_101", "Bus_202", "Bus_303", "Bus_404", "Bus_505"]

# Function to generate initial coordinates (example: near Gurugram, India)
def generate_initial_coordinates():
    lat = round(random.uniform(28.40, 28.50), 6)
    lon = round(random.uniform(77.00, 77.10), 6)
    return {"lat": lat, "lon": lon}

# Create initial positions for each bus
bus_data = {bus: generate_initial_coordinates() for bus in bus_ids}

# Function to simulate gradual movement
def move_bus(bus_pos):
    # Small movement in latitude and longitude
    delta_lat = round(random.uniform(-0.0005, 0.0005), 6)
    delta_lon = round(random.uniform(-0.0005, 0.0005), 6)
    bus_pos["lat"] = round(bus_pos["lat"] + delta_lat, 6)
    bus_pos["lon"] = round(bus_pos["lon"] + delta_lon, 6)
    return bus_pos

try:
    while True:
        # Update positions for each bus
        for bus in bus_data:
            bus_data[bus] = move_bus(bus_data[bus])

        # Save to JSON file
        with open("bus_locations.json", "w") as file:
            json.dump(bus_data, file, indent=4)

        print("Updated bus locations:", bus_data)
        time.sleep(5)  # Update every 5 seconds

except KeyboardInterrupt:
    print("\nSimulation stopped.")
