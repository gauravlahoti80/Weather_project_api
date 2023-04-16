from flask import Flask, render_template
from main import temperature, precipi, img, humidity, windspeed, new_cities, time
from aqi import air_quality_index

app = Flask(__name__, template_folder='./templates')

@app.route("/")
def home():
    return render_template("weather.html", city_name=new_cities, img=img, curr_temp=temperature, ws=windspeed, precipitation=precipi, humid=humidity, values=len(new_cities), curr_time = time, aqi = air_quality_index)

if __name__ == "__main__":
    app.run(debug=True)
