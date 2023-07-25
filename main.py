#ISS Location with Longitude and Latitude

import requests
import json

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)

# You can write if statements like this if you want for error code
# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")
# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data.")
# But instead of raising an exception for every status code possible you can do something like this:
response.raise_for_status()

data = response.json()
print(data)
longitude = data["iss_position"]["longitude"]
print(longitude)
latitude = data["iss_position"]["latitude"]
print(latitude)
iss_position = (longitude, latitude)
print(iss_position)

