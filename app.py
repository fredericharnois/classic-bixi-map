from flask import Flask, render_template, request
import requests
import json
import folium

app = Flask(__name__)

def get_bixi_data():
    info_url = "https://gbfs.velobixi.com/gbfs/en/station_information.json"
    status_url = "https://gbfs.velobixi.com/gbfs/en/station_status.json"

    station_info_response = requests.get(info_url)
    station_info = station_info_response.json()

    station_info_dict = {}
    for station in station_info["data"]["stations"]:
        station_id = station["station_id"]
        station_info_dict[station_id] = station

    station_status_response = requests.get(status_url)
    station_status = station_status_response.json()

    stations_list = []
    for station in station_status["data"]["stations"]:
        station_id = station["station_id"]
        num_classic_bikes_available = station["num_bikes_available"] - station["num_ebikes_available"]

        station_dict = {}
        if station_id in station_info_dict:
            station_info = station_info_dict[station_id]
            station_dict["name"] = station_info["name"]
            station_dict["lat"] = station_info["lat"]
            station_dict["lon"] = station_info["lon"]
            station_dict["classic_bikes"] = num_classic_bikes_available
            stations_list.append(station_dict)
        
    return stations_list

def create_marker(lat, lon, name, bikes, color, map):
    folium.Marker(
        location=[lat, lon],
        popup=f"""
        <b>{name}</b><br>
        Classic bikes: {bikes}
        """,
        icon=folium.Icon(color=color, icon="person-biking", prefix="fa"),
        tooltip=f"{name}: {bikes} classic bikes"
    ).add_to(map)

@app.route('/')
def index():
    user_lat = request.args.get("lat", type=float)
    user_lon = request.args.get("lon", type=float)
    
    default_lat, default_lon = 45.5088, -73.5878
    default_zoom = 12
    
    if user_lat and user_lon:
        map_center = [user_lat, user_lon]
        zoom_level = 15
    else:
        map_center = [default_lat, default_lon]
        zoom_level = default_zoom
    
    montreal_map = folium.Map(
        location=map_center,
        zoom_start=zoom_level,
        tiles="OpenStreetMap",
        width="100%",
        height= "100%"
    )
    
    if user_lat and user_lon:
        folium.Marker(
            location=[user_lat, user_lon],
            popup="📍 Your Location",
            icon=folium.Icon(color="blue", icon="user", prefix="fa"),
            tooltip="Your Location"
        ).add_to(montreal_map)
    
    stations = get_bixi_data()

    for station in stations:
        if station["classic_bikes"] == 0:
            create_marker(station["lat"], station["lon"], station["name"], station["classic_bikes"], "red", montreal_map)

        elif 0 < station["classic_bikes"] < 4:
            create_marker(station["lat"], station["lon"], station["name"], station["classic_bikes"], "orange", montreal_map)

        else:
            create_marker(station["lat"], station["lon"], station["name"], station["classic_bikes"], "green", montreal_map)
    
    map_html = montreal_map._repr_html_()
    return render_template("index.html", map_html=map_html)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)