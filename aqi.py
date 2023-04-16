import requests
import pandas as pd
from datetime import datetime, date, timedelta

air_quality_index = []
current_day = date.today()
current_date = current_day.strftime("%Y-%D-%M")
now = datetime.now()

def hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    round_time = str(t.replace(second=0, microsecond=0, minute=0, hour=t.hour)+timedelta(hours=t.minute//30))
    return round_time[11:-3]
final_curr_time = str(current_day)+'T'+hour_rounder(now)

latitude = []
longitude = []
df = pd.read_csv('in.csv')
for i in df['lat']:
    latitude.append(i)
for i in df['lng']:
    longitude.append(i)

for i in range(len(latitude)):
    api = f'https://air-quality-api.open-meteo.com/v1/air-quality?latitude={str(latitude[i])}&longitude={str(longitude[i])}&hourly=pm10,pm2_5'
    response = requests.get(api)
    json = response.json()
    # print(json)
    for i in json["hourly"]:
        for j in json["hourly"][i]:
            if j == final_curr_time:
                index = json["hourly"][i].index(j)
                air_quality_index.append(json["hourly"]["pm10"][int(index-1)])

print(air_quality_index)