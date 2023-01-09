api_key = "Enter Your Own Api Key" 
#you can get it from this website https://openweathermap.org/api
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = takeCommand().lower()
complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404":
	y = x["main"]
	current_temperature = y["temp"]
	current_pressure = y["pressure"]
	current_humidity = y["humidity"]
	z = x["weather"]
	weather_description = z[0]["description"]
	speak(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidity) +
		"\n description = " +
					str(weather_description))

else:
	speak(" City Not Found ")
