import requests

def getWeatherData(loc, dt, time):
    # REST endpoints
    WeatherAPI = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    PARAMS = {
        "key": "MTX4FE2YPSKCRNHR65QHVCUEW",
        "include": "current",
        "unitGroup": "metric"
    }
    location = str(loc)
    date = str(dt)
    time_str = str(time) + ":00"

    WeatherAPI += ("/" + location + "/" + date + "T" + time_str)

    try:
        # GET request
        req = requests.get(url=WeatherAPI, params=PARAMS)

        if req.status_code != 200:
            print("Error: API Status Code", req.status_code)
            # எரர் வந்தால் டீஃபால்ட் மதிப்புகளை அனுப்புவோம்
            return 0, 0, "Location Error", 25.0, 0.0

        data = req.json()

        # தரவுகள் இருக்கிறதா என சரிபார்ப்பு
        if "currentConditions" not in data or data["currentConditions"] is None:
             return 0, 0, "No Data", 25.0, 0.0

        latitude = data.get("latitude", 0)
        longitude = data.get("longitude", 0)
        formatted_address = data.get("resolvedAddress", str(loc))

        # Temperature Fix (பாதுகாப்பான முறை)
        temp_val = data["currentConditions"].get("temp")
        if temp_val is None:
            amb_temp = 25.0
        else:
            amb_temp = temp_val

        # Irradiation Fix (பாதுகாப்பான முறை)
        rad_val = data["currentConditions"].get("solarradiation")
        if rad_val is None:
            irradiation = 0.0
        else:
            irradiation = rad_val / 1000

        # மிக முக்கியம்: மதிப்புகளை திருப்பி அனுப்புதல்
        return latitude, longitude, formatted_address, amb_temp, irradiation

    except Exception as e:
        print(f"API Error: {e}")
        # ஏதாவது கிராஷ் ஆனால், பாதுகாப்பாக 0 மதிப்புகளை அனுப்பவும்
        return 0, 0, "API Error", 25.0, 0.0