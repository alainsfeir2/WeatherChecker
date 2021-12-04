
import pyowm # import Python Open Weather Map to our project.

APIKEY='33974b9e7113e4ce03abb04984bb1b26'    #your API Key here as string
OpenWMap=pyowm.OWM(APIKEY)                   # Use API key to get data
while (True):
	city = input("Enter City Name(exit enter 1):")
	if ( city == "1"):
		break
	else:
		Weatherforecast = OpenWMap.three_hours_forecast(str(city)) 
		Weather=OpenWMap.weather_at_place(str(city))  # give where you need to see the weather
		Data=Weather.get_weather()                   # get out data in the mentioned location

		humidity = Data.get_humidity() 		     	# get current humidity 
		temp = Data.get_temperature(unit='celsius')  	# get current temparature in celsius 
		wind = Data.get_wind() 			     	#get current wind 
		cloud = Data.get_clouds() 			# get current cloud
		rain=Weatherforecast.will_have_rain() # forecast rain
		sun=Weatherforecast.will_have_sun() # forecast sun
		cloud=Weatherforecast.will_have_clouds() # forecast clouds 

		print ("Average Temp. Currently ", temp['temp']) 	# get avg. tmp
		print ("Max Temp. Currently ", temp['temp_max']) 	# get max tmp
		print ("Min Temp. Currently ", temp['temp_min']) 	# get min tmp>>
		print ("Wind Speed : ",wind['speed']) 			# print wind speed
		print ("Wind Direction in Deg : ",wind['deg']) 		# print wind Direction
		print ("Cloud Coverage Percentage : ",cloud) 		# print cloud coverage percentage
		print ("Humidity : ",humidity) 				# print humidity 

		print("There will be rain :",rain) 			# print details
		print("There will be sun :",sun) 			#print details
		print("There will be clouds :",cloud) 			# print details
