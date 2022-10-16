import requests
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods = ['GET', 'POST'])
def locate():
    body = request.json
    # print(body)
    
    home = body["address"]
    mpg = int(body["mpg"])
    travel = body["travel"]
    total_car_dist = 0
    total_car_time = 0
    total_alt_time = 0
    travels = []
    travel_report = {}
    for place in travel:
        # print(place)
        place_address = place["address"]
        tpw = int(place["tpw"])
        car_dist, car_time = travel_info(home,place_address, tpw * 2, "driving")
        walk_dist, walk_time = travel_info(home,place_address, tpw * 2, "walking")
        bike_dist, bike_time = travel_info(home,place_address, tpw * 2, "bicycling")
        transit_dist, transit_time = travel_info(home,place_address, tpw * 2, "transit")
        
        place_report = {}
        place_report["address"] = place_address
        place_report["car_time"] = int(car_time / (60 * tpw * 2))
        place_report["car_dist"] = car_dist
        total_car_dist+=(car_dist * 0.000621371)
        total_car_time+=car_time
        
        if walk_time < (600 * tpw * 2) or (walk_time < bike_time and walk_time < transit_time):
            place_report["mode"] = "Walk"
            place_report["time"] = int(walk_time / (60 * tpw * 2))
            place_report["dist"] = int(walk_dist)
            total_alt_time+=walk_time
        elif bike_time < transit_time:
            place_report["mode"] = "Bike"
            place_report["time"] = int(bike_time / (60 * tpw * 2))
            place_report["dist"] = int(bike_dist)
            total_alt_time+=bike_time
        else:
            place_report["mode"] = "Transit"
            place_report["time"] = int(transit_time / (60 * tpw * 2))
            place_report["dist"] = int(transit_dist)
            total_alt_time+=transit_time
        travels.append(place_report)
    
    gasoline = total_car_dist / mpg
    gas_price = gasoline * 3.89
    co2_weight = gasoline * 20
    travel_report["car_time"] = int(total_car_time / 60)
    travel_report["alt_time"] = int(total_alt_time / 60)
    travel_report["gas_cost"] = int(gas_price)
    travel_report["emissions"] = int(co2_weight)
    travel_report["travels"] = travels
    
    report = jsonify(travel_report)     
    report.headers.add('Access-Control-Allow-Origin', '*')
    return report

def travel_info(home, place_address, tpw, type):
    travel = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin=" + home + "&destination=" 
                + place_address + "&key=AIzaSyALkVbxT1glbbW0tTp-IrAFye3q5i5PfXY&mode=" + type)
    travel_info = travel.json()
    legs = travel_info["routes"][0]["legs"][0]
    distance = legs["distance"]["value"]
    time = legs["duration"]["value"]
    
    return distance*tpw,time*tpw
