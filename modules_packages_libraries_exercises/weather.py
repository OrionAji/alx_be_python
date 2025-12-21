API_KEY = "ab310934b8ab7fb1694e725e3fbc76e3"
city = "Abuja"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
import urllib.request
import urllib.parse
import json

complete_url = base_url + "appid=" + API_KEY + "&q=" + urllib.parse.quote(city)

with urllib.request.urlopen(complete_url) as response:
    x = json.load(response)

if str(x.get("cod")) != "404":
    y = x.get("main", {})
    current_temperature = y.get("temp")
    current_pressure = y.get("pressure")
    current_humidity = y.get("humidity")
    z = x.get("weather", [])
    print(f"Temperature: {current_temperature}")
    print(f"Pressure: {current_pressure}")
    print(f"Humidity: {current_humidity}")
    if z:
        print(f"Weather description: {z[0].get('description')}")
else:
    print("City Not Found")
    