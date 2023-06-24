# Question:  Weather Forecasting Tool - Create a command line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.

#Load the required libraries
import requests
import json
import dotenv
import sys
import os
import random
from prettytable import PrettyTable

#create a function name asciart which print Asci art of WeThere
def asciart():
    art = """
__        __  _____ _                   
\ \      / /_|_   _| |__   ___ _ __ ___ 
 \ \ /\ / / _ \| | | '_ \ / _ \ '__/ _ \\
  \ V  V /  __/| | | | | |  __/ | |  __/
   \_/\_/ \___||_| |_| |_|\___|_|  \___| 
        The weather forecasting tool
    """
    print(art)

#load the environment variables
dotenv.load_dotenv()

#Get the API key from the environment variables
key = os.getenv("APIKEY")

#create a function name getWeather which takes city name as argument and return the weather details and also check for appropriate errors and print the error message
def getWeather(city, lengthARG):
    #check for valid city name
    fixparams = ["-t", "-c", "-f", "-k"]
    if city.isalpha():
        #create a variable url which store the url of the API with city name and API key
        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+key
        #create a variable response which store the response from the API

        response = requests.get(url)
        #check for valid response
        if response.status_code == 200:
            #create a variable data which store the data in json format
            data = response.json()

            #create a variable weather which store the weather details
            weather = data['weather'][0]['description']

            #create a variable temp which store the temperature
            temp = data['main']['temp']

            #create a variable humidity which store the humidity
            humidity = data['main']['humidity']

            #create a variable wind which store the wind speed
            wind = data['wind']['speed']

            #create a variable country which store the country name
            country = data['sys']['country']

            #create a variable city which store the city name
            city = data['name']

            deg = "K"

            #check for 3rd argument if it is -t then print the weather details in table format
            if lengthARG >= 3:
                if(lengthARG == 3 and sys.argv[2] not in fixparams):
                    #return the error message
                    return "Please enter the valid argument"
                if(lengthARG == 4 and (sys.argv[2] not in fixparams or sys.argv[3] not in fixparams)):
                    #return the error message
                    return "Please enter the valid argument"
                if(sys.argv[2] == "-t" and lengthARG == 3):
                    #use prettytable library to print the weather details in table format
                    table = PrettyTable()
                    table.field_names = ["City", "Country", "Weather", "Temperature", "Humidity", "Wind Speed"]
                    table.add_row([city, country, weather, str(temp)+"K", str(humidity)+"%", str(wind)+"m/s"])
                    return table
                #return temperature in celsius if 3rd argument is -c and in fahrenheit if 3rd argument is -f and in kelvin if 3rd argument is -k
                if(lengthARG == 4 and (sys.argv[2] == "-c" and sys.argv[3] == "-t") or (sys.argv[2] == "-t" and sys.argv[3] == "-c") or sys.argv[2] == "-c"):
                    #use prettytable library to print the weather details in table format
                    table = PrettyTable()
                    table.field_names = ["City", "Country", "Weather", "Temperature", "Humidity", "Wind Speed"]
                    table.add_row([city, country, weather, str(round(temp-273.15, 2))+"°C", str(humidity)+"%", str(wind)+"m/s"])
                    return table
                else:
                    temp = temp - 273.15
                    deg = "°C"
                
                if((lengthARG == 4 and sys.argv[2] == "-f" and sys.argv[3] == "-t") or (sys.argv[2] == "-t" and sys.argv[3] == "-f") or sys.argv[2] == "-f"):
                    #use prettytable library to print the weather details in table format
                    table = PrettyTable()
                    table.field_names = ["City", "Country", "Weather", "Temperature", "Humidity", "Wind Speed"]
                    table.add_row([city, country, weather, str(round((temp*9/5)+32, 2))+"°F", str(humidity)+"%", str(wind)+"m/s"])
                    return table
                else:
                    temp = (temp*9/5)+32
                    deg = "°F"
                
                if(lengthARG == 4 and (sys.argv[2] == "-k" and sys.argv[3] == "-t") or (sys.argv[2] == "-t" and sys.argv[3] == "-k") or sys.argv[2] == "-k"):
                    #use prettytable library to print the weather details in table format
                    table = PrettyTable()
                    table.field_names = ["City", "Country", "Weather", "Temperature", "Humidity", "Wind Speed"]
                    table.add_row([city, country, weather, str(round(temp, 2))+"K", str(humidity)+"%", str(wind)+"m/s"])
                    return table
                else:
                    temp = temp
                    deg = "K"
            #round off the temperature to 2 decimal places
            temp = round(temp, 2)
            #create a variable weatherDetails which store the weather details
            weatherDetails = "The weather in "+city+", "+country+" is "+weather+" with a temperature of "+str(temp)+str(deg)+", humidity of "+str(humidity)+"% and wind speed of "+str(wind)+"m/s"
            #return the weather details
            return weatherDetails

        #check for invalid response
        elif response.status_code == 404:
            #return the error message
            return "City not found"

        #check for invalid response
        elif response.status_code == 401:
            #return the error message
            return "Invalid API key"

        #check for invalid response
        elif response.status_code == 429:
            #return the error message
            return "Too many requests"

        #check for invalid response
        elif response.status_code == 500:
            #return the error message
            return "Internal server error"

        #check for invalid response
        elif response.status_code == 503:
            #return the error message
            return "Service unavailable"

        #check for invalid response
        elif response.status_code == 504:
            #return the error message
            return "Gateway timeout"

        #check for invalid response
        elif response.status_code == 502:
            #return the error message
            return "Bad gateway"

        #check for invalid response
        elif response.status_code == 400:
            #return the error message
            return "Bad request"
        else:
            #return the error message
            return "Something went wrong"
    else:
        #return the error message
        return "Please enter the valid city name"

#create a function name Whelp which print the help message
def Whelp():
    print(" \nUsage: forecast.py CITY [OPTIONS]\n \nOPTIONS:\n \n  -t, --table\t\t\tPrint the weather details in table format\n  -c, --celsius\t\t\tPrint the temperature in celsius\n  -f, --fahrenheit\t\tPrint the temperature in fahrenheit\n  -k, --kelvin\t\t\tPrint the temperature in kelvin\n  -h, --help\t\t\tPrint the help message\n \nEXAMPLES:\n \n  forecast.py London\n  forecast.py London -t\n  forecast.py London -c\n  forecast.py London -t -c\n  forecast.py London -t -f")

#create a function name footer which print the footer message
def footer():
    print(" ")
    print("Developed by: Rudra Shah")
    print("Github: https://github.com/Fastest-Coder-First/weThere")

#get length of the arguments
lengthARG = len(sys.argv)

#create a main function which call the asciart function, getWeather function and footer function
def main():
    asciart()
    #Get the city name from the user as argument and check for valid input
    if lengthARG >= 2:
        city = sys.argv[1]
        if(city=="-h" or city=="--help"):
            Whelp()
            exit()
        print(getWeather(city, lengthARG))
    else:
        print("Please enter the city name as argument")
        exit()
    footer()

#call the main function
if __name__ == "__main__":
    main()