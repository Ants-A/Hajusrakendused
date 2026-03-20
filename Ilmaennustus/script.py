import requests

header = {
    'User-Agent': 'school-project'
}
url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.436962&lon=24.753574"
response = requests.get(url, headers = header)
data = response.json()

for i in range(5):
    print(f"Time: {data['properties']['timeseries'][i]['time']} \n Weather: {data['properties']['timeseries'][i]['data']['instant']['details']['air_temperature']} C")
