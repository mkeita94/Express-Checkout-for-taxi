from datetime import*
from geopy import distance
from geopy.geocoders import Nominatim
#This program charges riders based on time and distance 
# and print their receipts

def calculate_cost(dist):
        #Constants
        REGULAR_INITIAL_FARE = 5.0
        RUSH_HOURS_INITIAL_FARE = 9.0
        OVERNIGHT_FARE = 7.0
        STATE_TAX = 0.06
        current_time = datetime.now()

        #Regular fare
        if(11 <= current_time.hour <= 15 or 21 <= current_time.hour <= 23):
                fare_type = "regular"
                print("-------Receipt-------")
                print("Distance: ", str(float("{0:.2f}".format(dist))), "miles")
                print("Fare type: ", fare_type)
                subtotal = REGULAR_INITIAL_FARE + dist
                print("Subtotal: $",str(float("{0:.2f}".format(subtotal))))
                tax = subtotal * STATE_TAX
                total = subtotal + tax
                print("Tax: $",str(float("{0:.2f}".format(tax))))
                print("Total: $",str(float("{0:.2f}".format(total))))
                print(current_time.strftime('%c'))
                #Rush hours
        elif(6 <= current_time.hour <= 10 or 16 <= current_time.hour <= 20 ):
                fare_type = "rush hours"
                print("-------Receipt-------")
                print("Distance: ", str(float("{0:.2f}".format(dist))), "miles")
                print("Fare type: ", fare_type)
                subtotal = RUSH_HOURS_INITIAL_FARE + dist
                print("Subtotal: $",str(float("{0:.2f}".format(subtotal))))
                tax = subtotal * STATE_TAX
                print("Tax: $",str(float("{0:.2f}".format(tax))))
                total = subtotal + tax
                print("Total: $",str(float("{0:.2f}".format(total))))
                print(current_time.strftime('%c'))
                #overnight
        else:
                fare_type = "OVERNIGHT_FARE"
                print("-------Receipt-------")
                print("Distance: ", str(float("{0:.2f}".format(dist))), "miles")
                print("Fare type: ", fare_type)
                subtotal = OVERNIGHT_FARE * dist
                print("Subtotal: $",str(float("{0:.2f}".format(subtotal))))
                tax = subtotal * STATE_TAX
                print("Tax: $",str(float("{0:.2f}".format(tax))))
                total = subtotal + tax
                print("Total: $",str(float("{0:.2f}".format(total))))
                print(current_time.strftime('%c'))
#Main program
#this program uses Geopy library to locate and calculate distance between two points
try:
	geolocator = Nominatim(user_agent="specify_your_app_name_here")
	print("----------------------------")
	print("| EXPRESS CHECK-OUT FOR TAXI|")
	print("----------------------------")
	starting_point = input("Enter your location: ")
	end_point = input("Enter your destination: ")
	location = geolocator.geocode(starting_point)
	destination = geolocator.geocode(end_point)

	print(location.address)
	print(destination.address)
	distance = distance.distance((location.latitude, location.longitude),(destination.latitude, destination.longitude))
	#Call function to print a receipt
	calculate_cost(distance.miles)
except Exception:
	print("Oops, Something went wrong.")
		
	
