#importing libraries
import requests
import pandas as pd


cities = []
df = pd.read_csv('in.csv')
for i in df['city']:
    cities.append(i)

#creating lists
new_cities = []
temperature = []
img = []
windspeed = []
precipi = []
humidity = []
time = []

#iterating over each element in list of cities
for i in cities:
    #api key and getting the data
    '''
        Please give your api key and then run the program. You can get one from weatherstack.com
    '''
    api = f'http://api.weatherstack.com/current?access_key=your_api_key&query={str(i)}'
    response = requests.get(str(api))
    parse_json = response.json()
   
    #for loop to get required values
    for i in parse_json:
        for j in parse_json[i]:
            if j == "temperature":
                temperature.append(parse_json[i][j])
            if j == "localtime":
                time.append(parse_json[i][j][10:])
            elif j == "weather_icons":
                for x in parse_json[i][j]:
                    img_url = ''
                    img_url = str(img_url + x)
                    img.append(img_url)
            elif j == "wind_speed":
                windspeed.append(parse_json[i][j])
            elif j == "humidity":
                humidity.append(parse_json[i][j])
            elif j == "query":
                new_cities.append(parse_json[i][j])
            elif j == "precip":
                precipi.append(parse_json[i][j])
