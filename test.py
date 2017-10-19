import time
from datetime import datetime, timedelta
from icalendar import Calendar, Event
import calendar
import forecastio


api_key = "d65a033e1b1486e87eb450cf04dbc992"
lat = 51.3612
lng = 1.4236

def forecast():
	weatherday1 = forecastio.load_forecast(api_key, lat, lng, time=datetime.now())
#	weatherday2 = forecastio.load_forecast(api_key, lat, lng, time=datetime.now()+timedelta(days=1))
#	weatherday3 = forecastio.load_forecast(api_key, lat, lng, time=datetime.now()+timedelta(days=2))
#	weatherday4 = forecastio.load_forecast(api_key, lat, lng, time=datetime.now()+timedelta(days=3))
#	weatherday5 = forecastio.load_forecast(api_key, lat, lng, time=datetime.now()+timedelta(days=4))


	byHour = weatherday1.currently()
	print(str(byHour.temperature) + ' ' + str(byHour.icon) + ' ' + str(byHour.summary) + ' ' + str(byHour.windSpeed))  ## current weather display

	byHour1 = weatherday1.hourly().data
	print(weatherday1.hourly().summary)
	print(weatherday1.hourly().icon)
	daystemp = []
	dayswind = []
	currenthour = int(time.strftime("%H"))
	for x in byHour1:
		daystemp.append(x.temperature)
		dayswind.append(x.windSpeed)
	hourvalue = 23 - currenthour 
	hourvalue = 24 - hourvalue
	print(daystemp[hourvalue])
	print(dayswind[hourvalue])
#
forecast()
